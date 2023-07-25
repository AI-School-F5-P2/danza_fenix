from sqlalchemy import func
from datetime import datetime
from connection.connection import *
from classes.models import Nivel
from fastapi.responses import JSONResponse
from classes.logger_niveles import Logger
from sqlalchemy.exc import SQLAlchemyError



def qw_get_niveles():
    try:
        niveles = session.query(Nivel).all()
        if len(niveles) == 0:
            Logger.info("Se han intentado mostrar los niveles, pero no hay ninguno.")
            return JSONResponse(content={"message": "No se han encontrado niveles"}, status_code=404)
        else:
            Logger.info("Se han encontrado niveles.")
            return niveles
    except Exception as e:
        Logger.error(f"No existe el nivel {niveles.nivel}.")
        return JSONResponse(content={"message":f"Error al consutar niveles .{e}"}, status_code=400) 
    
def qw_post_niveles(nivel_input):
    try:
        nivel_datos = Nivel(**nivel_input)
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nivel_datos.nivel).first()
        if nivel_existe is not None:
            Logger.info("El nivel ya existe.")
            return JSONResponse(content={"message":"El nivel ya existe"}, status_code=400) 
        session.add(nivel_datos)
        session.flush()
        session.commit()
        Logger.info("El nivel ya ha sido grabado.")
        return JSONResponse(content={"message": "El Nivel ha sido grabado"}, status_code=200)
    except Exception as e:
        Logger.error(f"No existe el rol {nivel_input}.")
        return JSONResponse(content={"message":f"Error al consutar niveles .{e}"}, status_code=400)

def qw_put_niveles(nombre_nivel, nivel_nuevo):
    try:
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nombre_nivel).first()
        if nivel_existe is None:
            Logger.info("El nivel no existe.")
            return JSONResponse(content={"message": "El nivel no existe."}, status_code=404)
        nivel_existe.nivel = nivel_nuevo
        session.commit()
        Logger.info("El nivel ha sido actualizado")
        return JSONResponse(content={"message": "El Nivel ha sido actualizado."}, status_code=200)
    except Exception as e:
        Logger.error(f"No existe el nivel {nombre_nivel}.")
        return JSONResponse(content={"message":f"Error al actualizar los niveles .{e}"}, status_code=400)

def qw_delete_niveles(nombre_nivel):
    try:
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nombre_nivel).first()
        if nivel_existe is None:
            Logger.info("El nivel no existe.")
            return JSONResponse(content={"message": "El nivel no existe."}, status_code=404)
        session.delete(nivel_existe)
        session.commit()
        Logger.info("El nivel ha sido apagado.")
        return JSONResponse(content={"message": "El Nivel ha sido apagado."}, status_code=200)
    except SQLAlchemyError as e:
    # Si se produce un error de la base de datos (por ejemplo, por la restricción de uso en otra tabla),
    # se registra un mensaje de error y se devuelve una respuesta con el código de estado 400 (Bad Request)
        Logger.error("No se puede apagar este Nivel porque esta relacionano con otras tablas.")
        return JSONResponse(content={"message": "No se puede apagar eso nivel porque existen cursos relacionado a él."}, status_code=400)

    except Exception as e:
        Logger.error(f"Error al apagar el nivel {nivel_existe}.")
        return JSONResponse(content={"message":f"Error al apagar los niveles .{e}"}, status_code=400)

def qw_get_nivel(nombre_nivel):
    try:
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nombre_nivel).first()
        if nivel_existe is None:
            Logger.info("El nivel no existe.")
            return JSONResponse(content={"message": "El nivel no existe."}, status_code=404)
        Logger.info("El nivel ha sido encontrado.")
        return nivel_existe
    except Exception as e:
        Logger.error(f"Error al consultar el nivel {nombre_nivel}.")
        return JSONResponse(content={"message":f"Error al consultar los niveles .{e}"}, status_code=400)