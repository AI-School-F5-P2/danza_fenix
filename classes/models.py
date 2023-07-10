from sqlalchemy import ForeignKey, Table, Column, CheckConstraint, String, Integer, Float, DateTime, Boolean, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

'''
# DEFINIMOS LAS TABLAS "PIVOTE" PARA LAS RELACIONES MUCHOS A MUCHOS
# Definir la tabla pivote cursos_niveles
cursos_niveles = Table('cursos_niveles', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('id_curso', Integer, ForeignKey('cursos.id')),
    Column('id_nivel', Integer, ForeignKey('niveles.id')),
    Column('created_at', DateTime),
    Column('updated_at', DateTime)
)
# Definir la tabla pivote cursos_profesores
cursos_profesores = Table('cursos_profesores', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('id_curso', Integer, ForeignKey('cursos.id')),
    Column('id_profesor', Integer, ForeignKey('profesores.id')),
    Column('created_at', DateTime),
    Column('updated_at', DateTime)
)
# Definir la tabla pivote estudios (alumnos, cursos, profesores)
estudios = Table('estudios', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('id_alumno', Integer, ForeignKey('alumnos.id')),
    Column('id_curso', Integer, ForeignKey('cursos.id')),
    Column('id_profesor', Integer, ForeignKey('profesores.id')),
    Column('fecha_inicio', DateTime),
    Column('fecha_final', DateTime),
    Column('relacion_activa', Integer, default = 0),
    Column('created_at', DateTime),
    Column('updated_at', DateTime)
)
# Definir la tabla pivote entre estudios y descuentos
estudios_descuentos = Table('estudios_descuentos', Base.metadata,
    Column('id_estudio', Integer, ForeignKey('estudios.id')),
    Column('id_descuento', Integer, ForeignKey('descuentos.id')),
    Column('created_at', DateTime),
    Column('updated_at', DateTime)
)
'''
# DEFINIMOS LAS CLASES DE LAS TABLAS MAESTRAS.
class Alumno(Base): # Tabla de alumnos
    __tablename__ = "alumnos"
    id = Column("id", Integer, primary_key = True, nullable = False)
    nombre = Column("nombre", String, nullable = False)
    dni = Column("dni", String, nullable = False)
    email = Column("email", String, nullable = False)
    nacimiento = Column("nacimiento", DateTime, nullable = False)
    descuento_familiar = Column("descuento_familiar", Integer,\
                                CheckConstraint('descuento_familiar IN (0, 1)',\
                                name = 'valid_descuento_familiar'), default = 0)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)

    #cursos = relationship("Curso", secondary = estudios, backref = "alumnos_cursos")
    #profesores = relationship("Profesor", secondary = estudios, backref = "alumnos_profesores")
    
    def __init__(self, nombre, dni, email, nacimiento, descuento_familiar):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.nacimiento = nacimiento
        self.descuento_familiar = descuento_familiar

    def __repr__(self):
        return f"Alumno {self.id} se llama {self.nombre}.El DNI es {self.dni} y el mail es {self.email}"

class Curso(Base): # Tabla de cursos
    __tablename__ = "cursos"
    id = Column("id", Integer, primary_key = True, nullable = False)
    nombre_curso = Column("nombre_curso", String, nullable = False)
    precio = Column("precio", Float(precision = 5, asdecimal = True, decimal_return_scale = 2), nullable = False)
    id_grupo = Column("id_grupo", Integer, ForeignKey("grupos.id"), nullable = False)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)
    
    #grupo = relationship("Grupo")  # Establecer la relación con la clase Grupo
    #niveles = relationship("Nivel", secondary = cursos_niveles, backref = "cursos")
    #profesores = relationship("Profesor", secondary = cursos_profesores, backref = "cursos")
    #alumnos = relationship("Alumno", secondary = estudios, backref = "cursos_alumnos")
    #titulares = relationship("Profesor", secondary = estudios, backref = "alumnos_profesores")
    
    def __init__(self, nombre_curso, precio, id_grupo):
        self.nombre_curso = nombre_curso
        self.precio = precio
        self.id_grupo = id_grupo

    def __repr__(self):
        return f"Curso {self.id} de {self.nombre_curso}. Pertenece al grupo {self.grupo.nombre_grupo}.El precio es {self.precio}"

class Descuento(Base):
    __tablename__ = "descuentos"
    id = Column("id", Integer, primary_key = True, nullable = False)
    concepto = Column("concepto", String, nullable = False)
    porcentaje = Column("porcentaje", Float(precision = 5, asdecimal = True, decimal_return_scale = 2), nullable = False)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)
    
    #estudios = relationship("Estudio", secondary=estudios, backref="descuentos")

    def __init__(self, concepto, porcentaje):
        self.concepto = concepto
        self.porcentaje = porcentaje
    
class Grupo(Base): # Tabla de grupos
    __tablename__ = "grupos"
    id = Column("id", Integer, primary_key = True, nullable = False)
    nombre_grupo = Column("nombre_grupo", String, nullable = False)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)
    
    def __init__(self, nombre_grupo):
        self.nombre_grupo = nombre_grupo
    
    def __repr__(self):
        return f"Grupo {self.id} llamado {self.nombre_grupo}."

class Nivel(Base): # Tabla de niveles
    __tablename__ = "niveles"
    id = Column("id", Integer, primary_key = True, nullable = False)
    nivel = Column("nivel", String, nullable = False)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)
    
    #cursos = relationship("Curso", secondary = cursos_niveles, backref = "niveles")

    def __init__(self, nivel):
        self.nivel = nivel
    
    def __repr__(self):
        return f"Nivel {self.id} llamado {self.nivel}."

class Profesor(Base): # Tabla de profesores
    __tablename__ = "profesores"
    id = Column("id", Integer, primary_key = True, nullable = False)
    nombre_profesor = Column("nombre_profesor", String, nullable = False)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)
    
    #cursos = relationship("Curso", secondary = cursos_profesores, backref = "profesores")
    #alumnos = relationship("Alumno", secondary = estudios, backref = "alumnos_profesores")
    #temarios = relationship("Curso", secondary = estudios, backref = "cursos_profesores")

    def __init__(self, nombre_profesor):
        self.nombre_profesor = nombre_profesor
    
    def __repr__(self):
        return f"Profesor {self.id} se llama {self.nombre_profesor}."

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column("id", Integer, primary_key = True, nullable = False)
    login = Column("login", String, nullable = False)
    email = Column("email", String, nullable = False)
    password = Column("password", String, nullable = False)
    rol_id = Column("rol_id", Integer, ForeignKey("roles.id"), nullable = False)
    activo = Column("activo", Integer,\
                                CheckConstraint('activo IN (0, 1)',\
                                name = 'valid_activo'), default = 1)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)

    def __init__(self, login, email, password, rol_id, activo):
        self.login = login
        self.email = email
        self.password = password
        self.rol_id = rol_id
        self.activo = activo
    
    def __repr__(self):
        return f"Usuario {self.id} tiene el login {self.login}."

class Rol(Base):
    __tablename__ = "roles"
    id = Column("id", Integer, primary_key = True, nullable = False)
    nombre_rol = Column("nombre_rol", String, nullable = False)
    created_at = Column("created_at", DateTime, nullable = False)
    updated_at = Column("updated_at", DateTime)
    
    def __init__(self, nombre_rol, created_at = datetime.now(), updated_at = datetime.now()):
        self.nombre_rol = nombre_rol
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return f"Rol {self.id} se llama {self.nombre_rol}."
