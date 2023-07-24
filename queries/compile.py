from sqlalchemy import func
from datetime import datetime
from connection.connection import *
from classes.models import Compile
from classes.models import Alumno
from classes.models import Curso
from fastapi.responses import JSONResponse
from fastapi import status

def qw_create_compile(compile_input):
    try:
        information = Compile(**compile_input)
        dni_select = information.dni_usuario
        alumno = session.query(Alumno).filter(Alumno.dni == dni_select).first()
        if alumno is None:
            return "El alumno no existe."
        session.add(information)
        session.flush()
        session.commit()
        out = "El alumno ha sido grabado."
    except Exception as e:
        return f"No se ha podido grabar el alumno.{e}"
    return out

def qw_mostrar_compile():
    information = session.query(Compile).all()
    if len(information) == 0:
        return "No se han encontrado alumnos."
    return information

def qw_create_compile(compile_input):
    try:
        information = Compile(**compile_input)
        dni_select = information.dni_usuario
        alumno = session.query(Alumno).filter(Alumno.dni == dni_select).first()
        if alumno is None:
            return "El alumno no existe."
        curso_actual = information.cursos
        curso = session.query(Curso).filter(Curso.nombre_curso == curso_actual).first()
        if curso is None:
            return "El curso no existe."
        precio_clase = curso.precio
        information.precio = precio_clase
        session.add(information)
        session.flush()
        session.commit()
        out = f"El alumno ha sido grabado. Precio de la clase: {precio_clase}"
    except Exception as e:
        return f"No se ha podido grabar el alumno.{e}"
    return out

def qw_mostrar_compile():
    information = session.query(Compile).all()
    if len(information) == 0:
        return "No se han encontrado alumnos."
    return information

# funcion para inscribir a un nuevo alumno y calcular el precio de la inscripcion
def wq_get_descuento(dni_alumno):
    # comprobacion de que el alumno existe
    information = session.query(Compile).filter(Compile.dni_usuario == dni_alumno).all()
    # si el alumno no existe, se devuelve un mensaje de error
    if information is None or len(information) == 0:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "No se han encontrado alumnos."})
    # se pregunta si el alumno tiene descuento familiar
    check_familiar = session.query(Alumno).filter(Alumno.dni == dni_alumno).first()
    total_precio = 0

    # se calcula el precio total de los cursos
    for info in information:
        total_precio += info.precio

    # si el alumno tiene descuento familiar, se le aplica un 10% de descuento
    if check_familiar.descuento_familiar == 1:
        descuento = total_precio * 0.1
        total_precio -= descuento

    # se devuelve el precio total
    return f"el total a pagar es de {total_precio} euros"