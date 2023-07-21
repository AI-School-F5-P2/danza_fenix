from fastapi import APIRouter
from classes.validations import InscripcionValidator
from classes.queries import qw_create_compile, qw_mostrar_compile, wq_get_descuento

router = APIRouter()

# funcion para insertar un nuevo curso
@router.post("/inscribir", tags=["inscripcion"])
def insertar_inscripcion(rol: InscripcionValidator):
    return qw_create_compile(rol.dict())

# esta funcion es para mostrar toda la informacion en al bbdd
@router.get("/listar_alumnos", tags=["inscripcion"])
def mostrar_inscripcion():
    return qw_mostrar_compile()

# funcion para mostrar un solo grupo
@router.get("/descuento", tags=["inscripcion"])
def mostrar_inscripcion(dni_alumno: str):
    return wq_get_descuento(dni_alumno)