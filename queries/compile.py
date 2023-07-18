from sqlalchemy import func
from datetime import datetime
from connection.connection import *
from classes.models import Compile
from classes.models import Alumno
# funcion para inscribir a un nuevo alumno

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

from sqlalchemy import func

def qw_get_curso(dni_alumno):
    information = session.query(Compile).filter(Compile.dni_usuario == dni_alumno).all()
    if information is None or len(information) == 0:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "No se han encontrado alumnos."})
    
    descuentos = {
        "Bachata": [0, 0.5, 0.75],
        "Salsa": [0, 0.5, 0.75],
        "Kizomba": [0, 0.5, 0.75],
        "Role": [0, 0.5, 0.75],
        "Estilo para todos": [0, 0.5, 0.75],
        "Lady": [0, 0.5, 0.75],
        "Pilates": [0, 0.5, 0.75],
        "Yoga": [0, 0.5, 0.75],
        "Zouk": [0, 0.5, 0.75]
    }

    precios = {
        "Bachata": 35,
        "Salsa": 35,
        "Kizomba": 35,
        "Role": 35,
        "Estilo para todos": 40,
        "Lady": 40,
        "Pilates": 40,
        "Yoga": 40,
        "Zouk": 40
    }

    cursos = {}

    for item in information:
        curso = item.cursos
        if curso in cursos:
            cursos[curso]["count"] += 1
            cantidad = cursos[curso]["count"]
            descuento_index = min(cantidad, 2)  # Índice para acceder al descuento correspondiente
            descuento = descuentos[curso][descuento_index]
            cursos[curso]["precio"] = precios[curso] * (1 - descuento)
        else:
            cursos[curso] = {"count": 1, "precio": precios[curso]}
    
    for curso, info in cursos.items():
        cantidad = info["count"]
        precio = info["precio"]
        print(f"Curso: {curso}, Cantidad: {cantidad}, Precio: {precio}€")

    return cursos

