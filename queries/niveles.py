from sqlalchemy import func
from datetime import datetime
from connection.connection import *
from classes.models import Nivel
from fastapi.responses import JSONResponse
from classes.logger import Logger


def qw_get_niveles():
    try:
        niveles = session.query(Nivel).all()
        if len(niveles) == 0:
            Logger.error(f"Se han intentado listar los niveles pero no hay ninguno.", "./logs/logs_niveles.txt")
            return JSONResponse(content={"message": "No se han encontrado niveles"}, status_code=404)
        else:
            Logger.info(f"Se han listado los niveles.", "./logs/logs_niveles.txt")
            return niveles
    except Exception as e:
        Logger.critical(f"Se han intentado listar los niveles pero se ha producido una excepción.", "./logs/logs_niveles.txt")
        return JSONResponse(content={"message":f"Error al consutar niveles .{e}"}, status_code=400) 
    
def qw_post_niveles(nivel_input):
    try:
        nivel_datos = Nivel(**nivel_input)
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nivel_datos.nivel).first()
        if nivel_existe is not None:
            Logger.error(f"Se ha intentado grabar el nivel {nivel_datos.nivel}, pero ya existe.", "./logs/logs_niveles.txt")
            return JSONResponse(content={"message":"El nivel ya existe"}, status_code=400) 
        session.add(nivel_datos)
        session.flush()
        session.commit()
        Logger.info(f"Se ha grabado el nivel {nivel_datos.nivel}.", "./logs/logs_niveles.txt")
        return JSONResponse(content={"message": "El Nivel ha sido grabado"}, status_code=200)
    except Exception as e:
        Logger.critical(f"Se ha producido una excepción al tratar de grabar el nivel {nivel_datos.nivel}.", "./logs/logs_niveles.txt")
        return JSONResponse(content={"message":f"Error al consutar niveles .{e}"}, status_code=400)

def qw_put_niveles(nombre_nivel, nivel_nuevo):
    try:
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nombre_nivel).first()
        if nivel_existe is None:
            Logger.error(f"Se ha intentado actualizar el nivel {nombre_nivel} pero no existe.", "./logs/logs_niveles.txt")
            return JSONResponse(content={"message": "El nivel no existe."}, status_code=404)
        nivel_existe.nivel = nivel_nuevo
        session.commit()
        Logger.info(f"Se ha actualizado el nivel {nombre_nivel} a {nivel_nuevo}.", "./logs/logs_niveles.txt")
        return JSONResponse(content={"message": "El Nivel ha sido actualizado."}, status_code=200)
    except Exception as e:
        Logger.critical(f"Se ha producido una excepción al tratar de actualizar el nivel {nombre_nivel}.", "./logs/logs_niveles.txt")
        return JSONResponse(content={"message":f"Error al actualizar los niveles .{e}"}, status_code=400)

def qw_delete_niveles(nombre_nivel):
    try:
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nombre_nivel).first()
        if nivel_existe is None:
            Logger.error(f"Se ha intentado borrar el nivel {nombre_nivel} pero no existe.", "./logs/logs_niveles.txt")
            return JSONResponse(content={"message": "El nivel no existe."}, status_code=404)
        session.delete(nivel_existe)
        session.commit()
        Logger.info(f"Se ha eliminado el nivel {nombre_nivel}.", "./logs/logs_niveles.txt")
        return JSONResponse(content={"message": "El Nivel ha sido apagado."}, status_code=200)
    except Exception as e:
        Logger.critical(f"Se ha intentado borrar el nivel {nombre_nivel} pero se ha producido una excepción", "./logs/logs_niveles.txt")
        return JSONResponse(content={"message":f"Error al apagar los niveles .{e}"}, status_code=400)

def qw_get_nivel(nombre_nivel):
    try:
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nombre_nivel).first()
        if nivel_existe is None:
            Logger.error(f"Se ha intentado ver el nivel {nombre_nivel} pero no existe.", "./logs/logs_niveles.txt")
            return JSONResponse(content={"message": "El nivel no existe."}, status_code=404)
        Logger.info(f"Se ha mostrado el nivel {nombre_nivel}.", "./logs/logs_niveles.txt")
        return nivel_existe
    except Exception as e:
        Logger.critical(f"Se ha intentado mostrar el nivel {nombre_nivel} pero se ha producido una excepción.", "./logs/logs_niveles.txt")
        return JSONResponse(content={"message":f"Error al consultar los niveles .{e}"}, status_code=400)