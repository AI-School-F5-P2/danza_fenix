from sqlalchemy import func
from datetime import datetime
from connection.connection import * 
from classes.models import Profesor


def qw_get_profesores():
    try:
        profesores = session.query(Profesor).all()
        if len(profesores) == 0:
            return "No hay datos"
        return profesores
    
    except Exception as e:
        return f"Error, no se pueden consultar los datos.{e}"


def qw_post_profesores(datos_profesor):
    profesor = Profesor(**datos_profesor)
    profesor_existe = session.query(Profesor).filter(Profesor.nombre_profesor == profesor.nombre_profesor).first()
    if profesor_existe is not None:
        return "El profesor/a ya existe."
    session.add(profesor)
    session.flush()
    session.commit()
    return "El profesor/a ha sido grabado."
    
def qw_put_profesores(nombre_profesor, nuevo_profesor):
    try:
        profesor = session.query(Profesor).filter(Profesor.nombre_profesor == nombre_profesor).first()
        if profesor is None:
            return "Profesor no existe"
        profesor.nombre_profesor = nuevo_profesor
        session.commit()

    except Exception as e: 
        return f"Error al modificar profesor/a. {e}"

    return "Profesor/a modificado."


def qw_delete_profesores(borrar_profesor):
    try:
        profesor = session.query(Profesor).filter(Profesor.nombre_profesor == borrar_profesor).first()
        if profesor is None:
            return "Profesor no existe"
        
        session.delete(profesor)
        session.commit()

    except Exception as e:
        return f"Error al eliminar profesor/a. {e}" 
    return "Profesor/a eliminado"