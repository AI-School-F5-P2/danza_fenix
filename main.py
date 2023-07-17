from fastapi import FastAPI
from starlette.responses import RedirectResponse
from apis.roles import router as roles_router
from apis.usuarios import router as usuarios_router
from apis.cursos import router as cursos_router
from apis.compile import router as compile_router

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
    },
    {
        "name": "cursos",
        "description": "Operaciones con cursos"
    },
    {
        "name": "inscripcion",
        "description": "Operaciones con inscripciones"
    }
]

app = FastAPI(openapi_tags=tags_metadata, description="API para la gestión de la escuela de danza Fenix")

# Registrar enrutadores
app.include_router(roles_router, prefix="/roles")
app.include_router(usuarios_router, prefix="/usuarios")
app.include_router(cursos_router, prefix="/cursos")
app.include_router(compile_router, prefix="/compile")

#################### MAIN #################

@app.get("/", tags=["main"])
def main():
    return RedirectResponse(url="/docs")
