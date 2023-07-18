from sqlalchemy import func
from datetime import datetime
from connection.connection import *
from classes.models import Alumno


#qw_get_alumnos, qw_post_alumnos, qw_put_alumnos, qw_delete_alumnos

def qw_get_alumnos():
    try:            
        alumnos = session.query(Alumno).all()
        if len(alumnos) == 0:
            return "no se han encontrado alumnos"
        return alumnos
    except Exception as e:
        return f"Error al consultar alumno.{e}"
    
    
def qw_get_alumno(dni_alumno):
    try:            
        alumno = session.query(Alumno).filter(Alumno.dni == dni_alumno).first()
        if alumno is None:
            return "no se han encontrado el alumno"
        return alumno
    except Exception as e:
        return f"Error al consultar alumno.{e}"    
    
def qw_post_alumnos(datos_alumno):
    try:
        alumno = Alumno(**datos_alumno)
        session.add(alumno)
        session.flush()
        session.commit()
        out = "Alumno agregado correctamente"
    except Exception as e:
        if str(type(e)) == "<class 'sqlalchemy.exc.IntegrityError'>":
            out = "El alumno ya existe."
        else:
            out = f"No se ha podido grabar el alumno.{e}"
    return out


def qw_put_alumnos(dni_alumno,alumno):
    try:
        alumno = Alumno(**alumno)
        data_alumno = session.query(Alumno).filter(Alumno.dni == dni_alumno).first()
        if data_alumno is None:
            return "No se a encontrado el alumno"
        data_alumno.nombre = alumno.nombre
        data_alumno.apellidos = alumno.apellidos
        data_alumno.descuento_familiar = alumno.descuento_familiar
        data_alumno.dni = alumno.dni
        data_alumno.email = alumno.email
        data_alumno.telefono = alumno.telefono
        data_alumno.nacimiento = alumno.nacimiento
        session.flush()
        session.commit()
        out = "Alumno actualizado correctamente"
    except Exception as e:
        if str(type(e)) == "<class 'sqlalchemy.exc.IntegrityError'>":
            out = "El alumno no se pudo actualizar."
        else:
            out = f"No se ha podido grabar el alumno.{e}"
    return out

def qw_delete_alumno(dni_eliminar_alumno):
    try:
        eliminar_alumno = session.query(Alumno).filter(Alumno.dni == dni_eliminar_alumno).first()
        if eliminar_alumno is None:
            return "No se encontró el alumno"
        session.delete(eliminar_alumno)
        session.commit()
        out = "Alumno eliminado correctamente"
    except Exception as e:
        out = f"No se pudo eliminar el alumno: {e}"
    return out