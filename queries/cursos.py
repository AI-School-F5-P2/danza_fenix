from sqlalchemy import func
from datetime import datetime
from connection.connection import *
from classes.models import Curso

############## CURSOS #################
# Crear un nuevo curso
def qw_create_curso(curso_input):
    try:
        curso = Curso(**curso_input)
        session.add(curso)
        session.flush()
        session.commit()
        out = "El curso ha sido grabado."
    except Exception as e:
        if str(type(e)) == "<class 'sqlalchemy.exc.IntegrityError'>":
            out = "El curso ya existe previamente."
        else:
            out = f"No se ha podido grabar el curso.{e}"
    return out


# mostrar todos lo  s cursos
def qw_get_cursos():
    cursos = session.query(Curso).all()
    if len(cursos) == 0:
        return "No se han encontrado cursos."
    return cursos

# funcion para mostrar un solo curso
def qw_mostrar_curso(nombre_del_curso):
    curso = session.query(Curso).filter(Curso.nombre_curso == nombre_del_curso).first()
    if curso is None:
        return "Error: El curso especificado no existe."
    return curso


# funcion para modificar un curso
def qw_update_curso(nombre_del_curso, nuevo_nombre, nuevo_precio):
    try:
        curso = session.query(Curso).filter(Curso.nombre_curso == nombre_del_curso).first()
        if curso is None:
            return "Error: El curso especificado no existe."
        curso.nombre_curso = nuevo_nombre
        curso.precio = nuevo_precio
        session.commit()
    except Exception as e:
        return f"No se ha podido modificar el curso.{e}"
    return "El curso ha sido modificado."

# funcion para borrar un curso
def qw_delete_curso(nombre_del_curso):
    try:
        curso = session.query(Curso).filter(Curso.nombre_curso == nombre_del_curso).first()
        if curso is None:
            return "Error: El curso especificado no existe."
        session.delete(curso)
        session.commit()    
    except Exception as e:
        return f"No se ha podido borrar el curso.{e}"
    return "El curso ha sido borrado."