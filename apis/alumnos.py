from fastapi import APIRouter
from classes.queries import qw_get_alumnos, qw_get_alumno, qw_post_alumnos, qw_put_alumnos, qw_delete_alumno
from classes.validations import AlumnoValidator

router = APIRouter()

@router.get("/mostrar_alumnos", tags = ["alumnos"])
def mostrar_alumnos():
    return qw_get_alumnos()


@router.get("/mostrar_alumno", tags = ["alumnos"])
def mostrar_alumno(dni_alumno: str):
    return qw_get_alumno(dni_alumno)



@router.post("/insertar", tags = ["alumnos"])
def insertar_alumnos(alumno: AlumnoValidator):
    return qw_post_alumnos(alumno.dict())



@router.put("/actualizar", tags = ["alumnos"])
def actualizar_alumnos(dni_alumno:str,alumno: AlumnoValidator):
    return qw_put_alumnos(dni_alumno, alumno.dict())



@router.delete("/eliminar", tags = ["alumnos"])
def eliminar_alumno(dni_eliminar_alumno:str):
    return qw_delete_alumno(dni_eliminar_alumno)


