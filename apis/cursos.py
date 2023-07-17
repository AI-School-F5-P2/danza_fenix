from fastapi import APIRouter
from classes.queries import qw_create_curso, qw_get_cursos, qw_update_curso, qw_delete_curso, qw_get_curso
from classes.validations import CursoValidator

router = APIRouter()

# funcion para mostrar todos los grupos
@router.get("/ver", tags=["cursos"])
def mostrar_cursos():
    return qw_get_cursos()

# funcion para mostrar un solo curso
@router.get("/ver/{nombre_del_curso}", tags=["cursos"])
def mostrar_curso(nombre_del_curso: str):
    return qw_get_curso(nombre_del_curso)

# funcion para insertar un nuevo curso
@router.post("/insertar", tags=["cursos"])
def insertar_cursos(rol: CursoValidator):
    return qw_create_curso(rol.dict())

# funcion para modificar un curso
@router.put("/actualizar", tags=["cursos"])
def modificar_cursos(nombre_del_curso: str, nuevo_nombre: str, nuevo_precio: float):
    return qw_update_curso(nombre_del_curso, nuevo_nombre, nuevo_precio)


@router.delete("/borrar", tags=["cursos"])
def borrar_curso(nombre: str):
    return qw_delete_curso(nombre)