from sqlalchemy import func
from datetime import datetime
from connection.connection import *
from classes.models import Nivel

def qw_get_niveles():
    try:
        niveles = session.query(Nivel).all()
        if len(niveles) == 0:
            return "No se han encontrado niveles"
        else:
            return niveles
    except Exception as e:
        return f"Error al consutar niveles .{e}"
    
def qw_post_niveles(nivel_input):
    try:
        nivel_datos = Nivel(**nivel_input)
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nivel_datos.nivel).first()
        if nivel_existe is not None:
            return "El nivel ya existe"
        session.add(nivel_datos)
        session.flush()
        session.commit()
        return "El Nivel ha sido grabado"
    except Exception as e:
        return f"Error al consutar niveles .{e}"

def qw_put_niveles(nombre_nivel, nivel_nuevo):
    try:
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nombre_nivel).first()
        if nivel_existe is None:
            return "El nivel no existe"
        nivel_existe.nivel = nivel_nuevo
        session.commit()
        return "El Nivel ha sido actualizado"
    except Exception as e:
        return f"Error al consutar niveles .{e}"


def qw_delete_niveles(nombre_nivel):
    try:
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nombre_nivel).first()
        if nivel_existe is None:
            return "El nivel no existe"
        session.delete(nivel_existe)
        session.commit()
        return "El Nivel ha sido eliminado"
    except Exception as e:
        return f"Error al consutar niveles .{e}"

def qw_get_nivel(nombre_nivel):
    try:
        nivel_existe = session.query(Nivel).filter(Nivel.nivel == nombre_nivel).first()
        if nivel_existe is None:
            return "El nivel no existe"
        return nivel_existe
    except Exception as e:
        return f"Error al consutar niveles .{e}"
