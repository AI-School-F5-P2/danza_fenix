from fastapi import APIRouter
from classes.queries import qw_get_niveles, qw_post_niveles, qw_delete_niveles, qw_put_niveles, qw_get_nivel
from classes.validations import NivelValidator
router = APIRouter()

@router.get("/mostrar_niveles", tags=["niveles"])
def mostrar_niveles():
    return qw_get_niveles()

@router.get("/busqueda_nivel", tags=["niveles"])
def busqueda_nivel(nombre_nivel: str):
    return qw_get_nivel(nombre_nivel)


@router.delete("/apagar_niveles", tags = ["niveles"])
def apagar_niveles(nombre_nivel):
    return qw_delete_niveles(nombre_nivel)


@router.put("/actualizar_niveles", tags=["niveles"])
def actualizar_niveles(nombre_nivel: str, nuevo_nivel: str):
    return qw_put_niveles(nombre_nivel, nuevo_nivel)

@router.post("/insertar_niveles", tags=["niveles"])
def insertar_niveles(nivel: NivelValidator):
    return qw_post_niveles(nivel.dict())
