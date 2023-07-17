from sqlalchemy import Column, String, Integer, DateTime, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Alumno(Base): # Tabla de alumnos
    __tablename__ = "alumnos"
    id = Column("id", Integer, primary_key = True, nullable = False)
    nombre = Column("nombre", String, nullable = False)
    apellido = Column("apellido", String, nullable = False)
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
    
    def __init__(self, nombre, dni, email, nacimiento, descuento_familiar, created_at = datetime.now(), updated_at = datetime.now()):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.nacimiento = nacimiento
        self.descuento_familiar = descuento_familiar
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"Alumno {self.id} se llama {self.nombre}.El DNI es {self.dni} y el mail es {self.email}"

