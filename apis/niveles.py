from fastapi import APIRouter
from classes.queries import qw_get_niveles, qw_post_niveles, qw_delete_niveles, qw_put_niveles, qw_get_nivel
from classes.validations import NivelValidator
router = APIRouter()

@router.get("/mostrar_niveles", tags=["Niveles"])
def mostrar_niveles():
    return qw_get_niveles()

@router.get("/busqueda_nivel/{nombre_nivel}", tags=["Niveles"])
def busqueda_nivel(nombre_nivel: str):
    return qw_get_nivel(nombre_nivel)


@router.delete("/apagar_niveles/{nombre_nivel}", tags = ["Niveles"])
def apagar_niveles(nombre_nivel):
    return qw_delete_niveles(nombre_nivel)


@router.put("/actualizar_niveles/{nombre_nivel}/{nuevo_nivel}", tags=["Niveles"])
def actualizar_niveles(nombre_nivel: str, nuevo_nivel: str):
    return qw_put_niveles(nombre_nivel, nuevo_nivel)

@router.post("/insertar_niveles", tags=["Niveles"])
def insertar_niveles(nivel: NivelValidator):
    return qw_post_niveles(nivel.dict())
