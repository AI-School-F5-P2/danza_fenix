from sqlalchemy import func
from datetime import datetime

from classes.models import Grupo, Curso
from connection.connection import *

############## GRUPOS #################
# Crear un nuevo grupo
def qw_create_grupo(grupo_input):
    grupo = Grupo(**grupo_input)
    grupo_existe = session.query(Grupo).filter(Grupo.nombre_grupo == grupo.nombre_grupo).first() # Obtener el rol correspondiente    
    if grupo_existe is not None:
        return "El grupo ya existe previamente."
    session.add(grupo)
    session.flush()
    session.commit()
    return "El grupo ha sido grabado."

# Localizar un grupo por su id o nombre
def qw_get_grupo(dato, valor):
    if dato == "id":
        id = int(valor)
        grupo = session.query(Grupo).get(id)
        if grupo is None:
            return "Error: El grupo especificado no existe."
    elif dato == "nombre":
        grupo = session.query(Grupo).filter(Grupo.nombre_grupo == valor).first() # Obtener el grupo correspondiente    
        if grupo is None:
            return "Error: El grupo especificado no existe."
    else:
        return "El tipo de dato especificado no existe."
    return grupo

# Listar todos los grupos.
def qw_list_grupos():
    grupos = session.query(Grupo).all()
    if len(grupos) == 0:
        return "No se han encontrado grupos."
    for grupo in grupos:
        num_cursos = session.query(func.count(Curso.id)).filter(Curso.id_grupo == grupo.id).scalar()
        grupo.num_cursos = num_cursos
    return grupos

# Actualizar un grupo por id o por su nombre actual.
def qw_update_grupo(dato, valor, nuevo_nombre):
    if dato == "id":
        id = int(valor)
        grupo = session.query(Grupo).get(id)
        if grupo is None:
            return "Error: El grupo especificado no existe."
    elif dato == "nombre":
        grupo = session.query(Grupo).filter(Grupo.nombre_grupo == valor).first() # Obtener el rol correspondiente    
        if grupo is None:
            return "Error: El grupo especificado no existe."
        id = grupo.id
    else:
        return "El tipo de dato especificado no existe."
    # Actualizar el nombre del rol
    grupo.nombre_grupo = nuevo_nombre
    grupo.updated_at = datetime.now()
    session.flush()
    session.commit() # Guardar los cambios en la base de datos
    return "El grupo ha sido actualizado."

# Borrar un grupo por su id o por su nombre si ningún curso lo tiene asignado
def qw_delete_grupo(dato, valor):
    if dato == "id":
        id = int(valor)
        grupo = session.query(Grupo).get(id)
        if grupo is None:
            return "Error: El grupo especificado no existe."
    elif dato == "nombre":
        grupo = session.query(Grupo).filter(Grupo.nombre_grupo == valor).first() # Obtener el grupo correspondiente    
        if grupo is None:
            return "Error: El grupo especificado no existe."
        id = grupo.id
    else:
        return "El tipo de dato especificado no existe."
    # Verificar si existen cursos con el grupo especificado
    cursos_con_grupo = session.query(func.count(Curso.id)).filter(Curso.id_grupo == id).scalar()
    if cursos_con_grupo > 0:
        return "Error: No se puede borrar el grupo porque existen cursos relacionados."
    # Si no hay cursos relacionados, proceder a borrar el rol
    session.delete(grupo)
    session.flush()
    session.commit()
    return "El grupo ha sido eliminado."


