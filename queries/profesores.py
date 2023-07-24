from sqlalchemy import func
from datetime import datetime
from connection.connection import * 
from classes.models import Profesor
from fastapi.responses import JSONResponse

from classes.logger_profesores import Logger


def qw_get_profesores():
    try:
        profesores = session.query(Profesor).all()
        if len(profesores) == 0:
            Logger.warning(f"El profesor/a especificado no existe. {profesores}")
            return JSONResponse(content={"message": "Error: El profesor/a especificado no existe."}, status_code=404)
        
    except Exception as e:
        Logger.error(f"Error {profesores} al consultar profesores.")
        return JSONResponse(content={"message": f"No se ha encontrar el profesor/a.{e}"}, status_code=400)
    Logger.info(f"El profesor/a ha sido Encontrado .{profesores}")
    return JSONResponse(content={"message": "El profesor/a ha sido Encontrado"}, status_code=202)


def qw_list_profesores():
    try:            
        profesores = session.query(Profesor).all()
        if len(profesores) == 0:
            Logger.warning(f"No se han encontrado los {profesores}")
            return JSONResponse(content={"message": "Error: El profesor/a especificado no existe."}, status_code=404)
    except Exception as e:
        Logger.error(f"Error {profesores} al consultar profesores.")
        return JSONResponse(content={"message": f"No se ha podido borrar el profesor/a.{e}"}, status_code=400)
    Logger.info(f"El profesor/a ha sido borrado.")
    return JSONResponse(content={"message": "El profesor/a ha sido borrado."}, status_code=202)



def qw_post_profesores(datos_profesor):
    try:
        profesor = Profesor(**datos_profesor)
        profesor_existe = session.query(Profesor).filter(Profesor.nombre_profesor == profesor.nombre_profesor).first()
        if profesor_existe is not None:
            Logger.warning(f"El profesor/a ya existe. {profesor}")
            return JSONResponse(content={"message": "El profesor/a ya existe."}, status_code=404)
        session.add(profesor)
        session.flush()
        session.commit()    
    except Exception as e:
        Logger.error(f"El profesor no ha podido ser grabado. {profesor}")
        return JSONResponse(content={"message": f"El profesor no ha podido ser grabado.{e}"}, status_code=400)
    Logger.info(f"El profesor/a ha sido grabado. El/la {profesor}")
    return JSONResponse(content={"message": "El profesor/a ha sido grabado."}, status_code=202)
    


def qw_put_profesores(nombre_profesor, nuevo_profesor):
    try:
        profesor = session.query(Profesor).filter(Profesor.nombre_profesor == nombre_profesor).first()
        if profesor is None:
            Logger.warning(f"El profesor ya existe. {profesor}")
            return JSONResponse(content={"message": "Error: El profesor ya existe."}, status_code=404)
        profesor.nombre_profesor = nuevo_profesor
        session.commit()
        
    except Exception as e:
        Logger.error(f"No se ha podido añadir el profesor/a. {profesor}")
        return JSONResponse(content={"message": f"No se ha podido añadir el profesor/a.{e}"}, status_code=400)
    Logger.info(f"El profesor/a ha sido añadir. {profesor}")
    return JSONResponse(content={"message": "El profesor/a ha sido modificado/a"}, status_code=202)

   
def qw_delete_profesores(borrar_profesor):
    try:
        profesor = session.query(Profesor).filter(Profesor.nombre_profesor == borrar_profesor).first()
        if profesor is None:
            Logger.warning(f"El profesor especificado no existe. {profesor}")
            return JSONResponse(content={"message": "Error: El profesor especificado no existe."}, status_code=404)
        session.delete(profesor)
        session.commit()
  
    except Exception as e:
        Logger.error(f"No se ha podido borrar el profesor/a. {profesor}")
        return JSONResponse(content={"message": f"No se ha podido borrar el profesor/a.{e}"}, status_code=400)
    Logger.info(f"El profesor/a ha sido borrado. {profesor}")
    return JSONResponse(content={"message": "El profesor/a ha sido borrado."}, status_code=202)