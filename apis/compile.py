from fastapi import APIRouter
from classes.validations import InscripcionValidator
from classes.queries import qw_create_compile, qw_mostrar_compile, wq_get_descuento

router = APIRouter()

# funcion para insertar un nuevo curso
<<<<<<< HEAD
@router.post("/insertar", tags=["Inscripcion"])
def insertar_inscripcion(rol: InscripcionValidator):
    return qw_create_compile(rol.dict())

# funcion para mostrar todos los grupos
@router.get("/mostrar", tags=["Inscripcion"])
=======
@router.post("/inscribir", tags=["inscripcion"])
def insertar_inscripcion(rol: InscripcionValidator):
    return qw_create_compile(rol.dict())

# esta funcion es para mostrar toda la informacion en al bbdd
@router.get("/listar_alumnos", tags=["inscripcion"])
>>>>>>> 015b98ac494e577d03dd6bc68573e4742f48fda8
def mostrar_inscripcion():
    return qw_mostrar_compile()

# funcion para mostrar un solo grupo
<<<<<<< HEAD
@router.get("/mostrar/{dni_alumno}", tags=["Inscripcion"])
def mostrar_inscripcion(dni_alumno: str):
    return qw_get_curso(dni_alumno)
=======
@router.get("/descuento", tags=["inscripcion"])
def mostrar_inscripcion(dni_alumno: str):
    return wq_get_descuento(dni_alumno)
>>>>>>> 015b98ac494e577d03dd6bc68573e4742f48fda8
