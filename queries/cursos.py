from sqlalchemy import func
from datetime import datetime
from connection.connection import *
from classes.models import Curso, Grupo
from fastapi.responses import JSONResponse

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

# mostrar todos los cursos
def qw_get_cursos():
    cursos = session.query(Curso).all()
    if len(cursos) == 0:
        return "No se han encontrado cursos."
    cursos_dict = []
    for curso in cursos:
        grupo = session.query(Grupo).filter(Grupo.id == curso.id_grupo).first()
        curso_dict = {
            "id": curso.id,
            "nombre_curso": curso.nombre_curso,
            "nombre_grupo": grupo.nombre_grupo,
            "precio": curso.precio,
            "created_at": curso.created_at,
            "updated_at": curso.updated_at
        }
        cursos_dict.append(curso_dict)
    return cursos_dict

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
						# segundo paso en el return metemos el JSONResponse() dentro el mensaje y despues del status code
            return JSONResponse(content={"message": "Error: El curso especificado no existe."}, status_code=404)
        session.delete(curso)
        session.commit()    
    except Exception as e:
        return JSONResponse(content={"message": f"No se ha podido borrar el curso.{e}"}, status_code=400)
    return JSONResponse(content={"message": "El curso ha sido borrado."}, status_code=202)