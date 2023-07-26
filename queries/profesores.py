from sqlalchemy import func
from datetime import datetime
from connection.connection import * 
from classes.models import Profesor
from fastapi.responses import JSONResponse

def qw_get_profesores():
    try:
        profesores = session.query(Profesor).all()
        if len(profesores) == 0:
            return "No hay datos"
        return profesores      
        
    except Exception as e:
        return JSONResponse(content={"message": f"No se ha encontrar el profesor/a.{e}"}, status_code=400)
    return JSONResponse(content={"message": "El profesor/a ha sido Encontrado"}, status_code=202)

def qw_list_profesores(nombre_profesor):
    try:
        profesores = session.query(Profesor).filter(Profesor.nombre_profesor.like(f"%{nombre_profesor}%")).all()
        if len(profesores) == 0:
            return "No hay datos"
        return profesores
    except Exception as e:
        return JSONResponse(content={"message": f"No se ha encontrar el profesor/a.{e}"}, status_code=400)
 

def qw_post_profesores(datos_profesor):
    try:
        profesor = Profesor(**datos_profesor)
        profesor_existe = session.query(Profesor).filter(Profesor.nombre_profesor == profesor.nombre_profesor).first()
        if profesor_existe is not None:
            return JSONResponse(content={"message": "El profesor/a ya existe."}, status_code=404)
        session.add(profesor)
        session.flush()
        session.commit()    
    except Exception as e:
        return JSONResponse(content={"message": f"El profesor no ha podido ser grabado.{e}"}, status_code=400)
    return JSONResponse(content={"message": "El profesor/a ha sido grabado."}, status_code=202)
    
def qw_put_profesores(nombre_profesor, nuevo_profesor):
    try:
        profesor = session.query(Profesor).filter(Profesor.nombre_profesor == nombre_profesor).first()
        if profesor is None:
            return JSONResponse(content={"message": "Error: El profesor especificado no existe."}, status_code=404)
        profesor.nombre_profesor = nuevo_profesor
        session.commit()
    except Exception as e:
        return JSONResponse(content={"message": f"No se ha podido actualizar el profesor/a.{e}"}, status_code=400)
    return JSONResponse(content={"message": "El profesor/a ha sido actualizado."}, status_code=202)

def qw_delete_profesores(borrar_profesor):
    try:
        profesor = session.query(Profesor).filter(Profesor.nombre_profesor == borrar_profesor).first()
        if profesor is None:
            return JSONResponse(content={"message": "Error: El profesor especificado no existe."}, status_code=404)
        session.delete(profesor)
        session.commit()
    except Exception as e:
        return JSONResponse(content={"message": f"No se ha podido borrar el profesor/a.{e}"}, status_code=400)
    return JSONResponse(content={"message": "El profesor/a ha sido borrado."}, status_code=202)
