from fastapi import APIRouter
from classes.queries import qw_get_profesores, qw_post_profesores, qw_put_profesores, qw_delete_profesores
from classes.validations import ProfesorValidator

router = APIRouter()

@router.get("/ver", tags = ["Profesores"])
def mostrar_profesores ():
    return qw_get_profesores()

@router.post("/insertar", tags = ["Profesores"])
def insertar_profesor(profesor: ProfesorValidator):
    return qw_post_profesores(profesor.dict())

@router.put("/actualizar", tags = ["Profesores"])
def actualizar_profesor(profesor: str, nuevo_profesor: str):
    return qw_put_profesores(profesor, nuevo_profesor)

@router.delete("/eliminar", tags = ["Profesores"])
def eliminar_profesor(profesor: str):
    return qw_delete_profesores(profesor)