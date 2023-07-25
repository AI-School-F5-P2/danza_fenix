from fastapi import APIRouter
from classes.validations import InscripcionValidator
from classes.queries import qw_create_compile, qw_mostrar_compile, wq_get_descuentos, qw_mostrar_curso

router = APIRouter()

# funcion para insertar un nuevo curso
@router.post("/insertar", tags=["Inscripcion"])
def insertar_inscripcion(rol: InscripcionValidator):
    return qw_create_compile(rol.dict())

# # funcion para mostrar todos los grupos
# @router.get("/mostrar_inscripciones", tags=["Inscripcion"])
# def mostrar_inscripciones():
#     return qw_mostrar_curso()

# funcion para mostrar un solo grupo
# @router.get("/mostrar/{dni_alumno}", tags=["Inscripcion"])
# def mostrar_unica_inscripcion(dni_alumno: str):
#     return wq_get_descuentos(dni_alumno)


# ruta para generar el descuento 
@router.get("/descuento", tags=["Inscripcion"])
def mostrar_inscripcion(dni_alumno: str):
    return wq_get_descuentos(dni_alumno)
