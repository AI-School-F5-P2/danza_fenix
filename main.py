from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from classes.queries import *
from classes.validations import RolValidator

tags_metadata = [
    {
        "name":"main",
        "description":"Main area"
    },
    {
        "name":"roles",
        "description": "Operaciones con roles"
    }
]
app = FastAPI(openapi_tags = tags_metadata)

@app.get("/", tags = ["main"])
def main():
    return "Bienvenido a Danza Fenix"

@app.get("/roles/listar", tags = ["roles"])
def roles_listar():
    return qw_list_roles()

@app.get("/roles/ver_id/{id}", tags = ["roles"])
def roles_ver_por_id(id):
    return qw_get_rol_by_id(id)

@app.get("/roles/ver_nombre/{nombre}", tags = ["roles"])
def roles_ver_por_nombre(nombre):
    return qw_get_roles_by_name(nombre)

@app.post("/roles/insertar", tags = ["roles"])
def roles_insertar(rol:RolValidator):
    return qw_create_rol(rol.dict())

@app.put("/roles/actualizar_by_id", tags = ["roles"])
def roles_actualizar(id:int, nuevo_nombre:str):
    return qw_update_rol_by_id(id, nuevo_nombre)

@app.put("/roles/actualizar_by_name", tags = ["roles"])
def roles_actualizar(nombre:str, nuevo_nombre:str):
    return qw_update_rol_by_name(nombre, nuevo_nombre)

@app.delete("/roles/borrar_by_id", tags = ["roles"])
def roles_borrar(id:int):
    return qw_delete_rol_by_id(id)

@app.delete("/roles/borrar_by_name", tags = ["roles"])
def roles_borrar(name:str):
    return qw_delete_rol_by_name(name)

