from sqlalchemy import create_engine, or_, func
from sqlalchemy.orm import sessionmaker
from classes.models import Alumno, Curso, Descuento, Grupo, Nivel, Profesor, Usuario, Rol, Base
from classes.validations import UserValidator
from classes.encryption import Encryption
from datetime import datetime
import json

# Creamos la referencia al motor de base de datos
engine = create_engine('mysql+mysqlconnector://root:@localhost/danza_fenix', echo = True)
Base.metadata.create_all(bind=engine)

# Creamos la sesión para luego poder pasar las consultas.
Session = sessionmaker(bind = engine)
session = Session()

###################### Todas las funciones empiezan con el prefijo qw_ (de queries) #####################

############## ROLES #################
# Crear un nuevo rol
def qw_create_rol(rol_input):
    try:
        rol = Rol(**rol_input)
        session.add(rol)
        session.flush()
        session.commit()
        out = "El rol ha sido grabado."
    except Exception as e:
        if str(type(e)) == "<class 'sqlalchemy.exc.IntegrityError'>":
            out = "El rol ya existe previamente."
        else:
            out = f"No se ha podido grabar el rol.{e}"
    return out

# Localizar un rol por su id
def qw_get_rol_by_id(id):
    rol = session.query(Rol).get(id)
    if rol is None:
        return "Error: El rol especificado no existe."
    return rol

# Localizar roles por parte de su nombre
def qw_get_roles_by_name(name_part):
    roles = session.query(Rol).filter(Rol.nombre_rol.ilike('%' + name_part  + '%')).all()
    if len(roles) == 0:
        return "No se han encontrado coincidencias."
    return roles

# Listar todos los roles.
def qw_list_roles():
    roles = session.query(Rol).all()
    if len(roles) == 0:
        return "No se han encontrado roles."
    for rol in roles:
        num_usuarios = session.query(func.count(Usuario.id)).filter(Usuario.rol_id == rol.id).scalar()
        rol.num_usuarios = num_usuarios
    return roles

# Actualizar un rol por id
def qw_update_rol_by_id(id, nuevo_nombre):
    rol = session.query(Rol).get(id) # Obtener el rol correspondiente    
    # Verificar si el rol existe
    if rol is None:
        return "Error: El rol especificado no existe."    
    # Actualizar el nombre del rol
    rol.nombre_rol = nuevo_nombre
    rol.updated_at = datetime.now()
    session.flush()
    session.commit() # Guardar los cambios en la base de datos
    return "El rol ha sido actualizado."

# Actualizar un rol por nombre
def qw_update_rol_by_name(nombre, nuevo_nombre):
    rol = session.query(Rol).filter(Rol.nombre_rol == nombre).first() # Obtener el rol correspondiente    
    # Verificar si el rol existe
    if rol is None:
        return "Error: El rol especificado no existe."    
    # Actualizar el nombre del rol
    rol.nombre_rol = nuevo_nombre
    rol.updated_at = datetime.now()
    session.flush()
    session.commit() # Guardar los cambios en la base de datos
    return "El rol ha sido actualizado."

# Borrar un rol por su id si ningún usuario lo tiene asignado
def qw_delete_rol_by_id(id):
    # Verificar si existen usuarios con el rol especificado
    usuarios_con_rol = session.query(func.count(Usuario.id)).filter(Usuario.rol_id == id).scalar()
    if usuarios_con_rol > 0:
        return "Error: No se puede borrar el rol porque existen usuarios relacionados."
    # Si no hay usuarios relacionados, proceder a borrar el rol
    rol = session.query(Rol).get(id)
    if rol is None:
        return "Error: El rol especificado no existe."
    session.delete(rol)
    session.flush()
    session.commit()
    return "El rol ha sido eliminado."

# Borrar un rol por su nombre si ningún usuario lo tiene asignado
def qw_delete_rol_by_name(nombre_rol):
    # Buscar el rol por su nombre
    rol = session.query(Rol).filter(Rol.nombre_rol == nombre_rol).first()
    if rol is None:
        return "Error: No se encontró el rol especificado."
    # Verificar si existen usuarios con el rol especificado
    id = rol.id
    usuarios_con_rol = session.query(func.count(Usuario.id)).filter(Usuario.rol_id == id).scalar()
    if usuarios_con_rol > 0:
        return "Error: No se puede borrar el rol porque existen usuarios relacionados."
    # Si no hay usuarios relacionados, proceder a borrar el rol
    session.delete(rol)
    session.flush()
    session.commit()
    return "El rol ha sido eliminado."

############## USUARIOS #################
# Crear un nuevo usuario
def qw_create_usuario(usuario):
    rol = session.query(Rol).filter(Rol.nombre_rol == usuario.nombre_rol).first() # Buscar el rol por su nombre
    # Si no existe el rol se obtienen un mensaje de error.
    if not rol:
        return "El rol especificado no existe."
    rol_id = rol.id # Obtener el ID del rol
    # Crear el nuevo objeto de Usuario con el ID del rol
    pw = Encryption.encrypt(usuario.password)
    login_existe = session.query(Usuario).filter(Usuario.login == usuario.login).first()
    if login_existe:
        return "El login ya existe."
    email_existe = session.query(Usuario).filter(Usuario.email == usuario.email).first()
    if login_existe:
        return "El email ya existe."
    nuevo_usuario = Usuario(login = usuario.login, email = usuario.email, password = pw, rol_id = rol_id, created_at = datetime.now(), updated_at = datetime.now())
    session.add(nuevo_usuario) # Agregar el nuevo usuario a la sesión
    session.flush()
    session.commit() # Realizar el commit para persistir los cambios
    return "Usuario creado exitosamente."

# Listar todos los usuarios, indicando a cada uno el nombre de su rol
def qw_list_usuarios():
    # Obtenemos la lista de usuarios, incluyendo el nombre de su rol
    usuarios = session.query(Usuario, Rol.nombre_rol).join(Rol, Usuario.rol_id == Rol.id).all()
    if len(usuarios) == 0:
        return "No hay usuarios registrados."
    result = []
    for usuario, nombre_rol in usuarios:
        usuario_dict = {
            "id": usuario.id,
            "login": usuario.login,
            "email": usuario.email,
            "rol": nombre_rol
        }
        result.append(usuario_dict)
    return result

# Listar los datos de un usuario localizado a partir de un dato, que puede 
# ser el id, el login o el email.
def qw_show_usuario(dato, valor):
    if dato == "id":
        resultado = session.query(Usuario, Rol.nombre_rol).join(Rol, Usuario.rol_id == Rol.id).filter(Usuario.id == valor).first()
    elif dato == "login":
        resultado = session.query(Usuario, Rol.nombre_rol).join(Rol, Usuario.rol_id == Rol.id).filter(Usuario.login.ilike(f"%{valor}%")).all()
    elif dato == "email":
        resultado = session.query(Usuario, Rol.nombre_rol).join(Rol, Usuario.rol_id == Rol.id).filter(Usuario.email.ilike(f"%{valor}%")).all()
    else:
        return "Dato no válido."
    if not resultado:
        return "No se han encontrado usuarios."
    return resultado

# Actualizar los datos de un usuario localizado a partir de un dato, que puede 
# ser el id, el login o el email.
def qw_update_usuario(dato, valor, login, email, password, activo, nombre_rol):
    if dato == "id":
        usuario = session.query(Usuario).filter(Usuario.id == valor).first()
    elif dato == "login":
        usuario = session.query(Usuario).filter(Usuario.login.ilike(f"%{valor}%")).first()
    elif dato == "email":
        usuario = session.query(Usuario).filter(Usuario.email.ilike(f"%{valor}%")).first()
    else:
        return "Dato no válido."
    if not usuario:
        return "No se ha encontrado el usuario."
    # Verificamos si existe el rol
    rol = session.query(Rol).filter(Rol.nombre_rol == nombre_rol).first() # Buscar el rol por su nombre
    # Si no existe el rol se obtiene un mensaje de error.
    if not rol:
        return "El rol especificado no existe."
    rol_id = rol.id # Obtener el ID del rol
    pw = Encryption.encrypt(password) # Encriptamos la contraseña
    usuario.login = login
    usuario.email = email
    usuario.password = pw
    usuario.rol_id = rol_id
    usuario.activo = activo
    usuario.updated_at = datetime.now()
    session.flush()
    session.commit()
    return "El usuario ha sido actualizado."

# Eliminare un usuario localizado a partir de un dato, que puede 
# ser el id, el login o el email.
def qw_delete_usuario(dato, valor):
    if dato == "id":
        usuario = session.query(Usuario).filter(Usuario.id == valor).first()
    elif dato == "login":
        usuario = session.query(Usuario).filter(Usuario.login.ilike(f"%{valor}%")).first()
    elif dato == "email":
        usuario = session.query(Usuario).filter(Usuario.email.ilike(f"%{valor}%")).first()
    else:
        return "Dato no válido."
    if not usuario:
        return "No se ha encontrado el usuario."
    session.delete(usuario)
    session.flush()
    session.commit()
    return "El usuario ha sido eliminado."



'''
# EJEMPLOS DE USO.

# CREAR REGISTROS
# Crear un nivel
#nivel = Nivel(nivel="Básico", created_at=datetime.now()) # Definimos los datos, excepto el id, que es clave primaria autoincrementable.
#session.add(nivel) # Añadimos el objeto a la sesión para poder pasarlo a la base de datos.
#session.commit() # Commiteamos para persistir el objeto en la base de datos.
# Crear un alumno, sin especificar todos los campos:
#alumno = Alumno(nombre="John Doe", email="johndoe@example.com", descuento_familiar=False)
#session.add(alumno) # Añadimos el objeto a la sesión para poder pasarlo a la base de datos.
#session.commit() # Commiteamos para persistir el objeto en la base de datos.

# LEER REGISTROS
# Leer todos los registros de una tabla
#resultados = session.query(Nivel).all()
#print (resultados)
# Los datos se obtienen en una lista de registros.
# Las claúsulas WHERE de SQL se especifican con filter, así:
#resultados = session.query(Nivel).filter(id > 4).all()
# Un ejemplo más complejo. Todos los alumnos que tengan un email de gmail.com y el descuento_familiar activado:
#alumnos = session.query(Alumno).filter(Alumno.email.like('%@gmail.com%'), Alumno.descuento_familiar == True).all()
# Si queremos unir las claúsulas mediante or en vez de and, lo haremos así:
#alumnos = session.query(Alumno).filter(or_(Alumno.email.like('%@gmail.com%'), Alumno.descuento_familiar == True)).all()
'''


