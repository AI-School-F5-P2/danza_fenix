from fastapi import APIRouter
from classes.validations import InscripcionValidator
from classes.queries import qw_create_compile, qw_mostrar_compile, qw_get_curso

router = APIRouter()

# funcion para insertar un nuevo curso
@router.post("/insertar", tags=["Inscripcion"])
def insertar_inscripcion(rol: InscripcionValidator):
    return qw_create_compile(rol.dict())

# funcion para mostrar todos los grupos
@router.get("/mostrar", tags=["Inscripcion"])
def mostrar_inscripcion():
    return qw_mostrar_compile()

# funcion para mostrar un solo grupo
@router.get("/mostrar/{dni_alumno}", tags=["Inscripcion"])
def mostrar_inscripcion(dni_alumno: str):
    return qw_get_curso(dni_alumno)
