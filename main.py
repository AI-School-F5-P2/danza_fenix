from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
#from classes.queries import *
from classes.validations import RolValidator, UserValidator
from apis.roles import router as roles_router
from apis.usuarios import router as usuarios_router

tags_metadata = [
    {
        "name": "main",
        "description": "Main area"
    },
    {
        "name": "roles",
        "description": "Operaciones con roles"
    },
    {
        "name": "usuarios",
        "description": "Operaciones con usuarios"
    }
]

app = FastAPI(openapi_tags=tags_metadata)

# Registrar enrutadores
app.include_router(roles_router, prefix="/roles")
app.include_router(usuarios_router, prefix="/usuarios")

#################### MAIN #################
@app.get("/", tags=["main"])
def main():
    return RedirectResponse(url="/docs")
