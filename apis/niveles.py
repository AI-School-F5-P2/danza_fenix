from fastapi import APIRouter
from classes.queries import qw_get_niveles, qw_post_niveles, qw_delete_niveles, qw_put_niveles, qw_get_nivel
from classes.validations import NivelValidator
router = APIRouter()

@router.get("/mostrar_niveles", tags=["niveles"])
def mostrar_niveles():
    """<h1>Método para mostrar todos los niveles.</h1>
    <p>Este método devolve todos los niveles registrados al usuario.</p>"""
    return qw_get_niveles()

@router.get("/busqueda_nivel", tags=["niveles"])
def busqueda_nivel(nombre_nivel: str):
    """<h1>Método para buscar uno unico nivel.</h1>
    <p>Este método devolve el nivel buscado el usuario.</p>"""
    return qw_get_nivel(nombre_nivel)


@router.delete("/apagar_niveles", tags = ["niveles"])
def apagar_niveles(nombre_nivel):
    """<h1>Método para apagar niveles.</h1>
    <p>Este método permite el al usuario apagar el nivel deseado.</p>"""
    return qw_delete_niveles(nombre_nivel)


@router.put("/actualizar_niveles", tags=["niveles"])
def actualizar_niveles(nombre_nivel: str, nuevo_nivel: str):
    """<h1>Método para actualizar niveles.</h1>
    <p>Este método permite al usuario modificar la description de los niveles.</p>"""
    return qw_put_niveles(nombre_nivel, nuevo_nivel)

@router.post("/insertar_niveles", tags=["niveles"])
def insertar_niveles(nivel: NivelValidator):
    """<h1>Método para insertar niveles.</h1>
    <p>Este método permite al usuario insertar nuevos niveles.</p>"""
    return qw_post_niveles(nivel.dict())
