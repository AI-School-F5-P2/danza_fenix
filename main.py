from fastapi import FastAPI
from starlette.responses import RedirectResponse
from apis.roles import router as roles_router
from apis.usuarios import router as usuarios_router
from apis.alumnos import router as alumnos_router 
from apis.niveles import router as niveles_router
from apis.profesores import router as profesores_router
from apis.cursos import router as cursos_router
from apis.estudios import router as estudios_router
from apis.grupos import router as grupos_router

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
        "name": "alumnos",
        "description": "Operaciones de alumnos"
    },

    {
        "name": "niveles",
        "description": "Operaciones con niveles"
    },
    {

        "name": "profesores",
        "description" : "Operaciones con profesores"
    },
    {
        "name": "cursos",
        "description": "Operaciones con cursos"
    },
    {
        "name": "inscripcion",
        "description": "Operaciones con inscripciones"
    },
    {
        "name": "grupos",
        "description": "Operaciones con grupos"
    }
]

app = FastAPI(openapi_tags=tags_metadata, description="API para la gestión de la escuela de danza Fenix")

# Registrar enrutadores
app.include_router(roles_router, prefix="/roles")
app.include_router(usuarios_router, prefix="/usuarios")
app.include_router(alumnos_router, prefix ="/alumnos")

app.include_router(niveles_router, prefix = "/niveles")
app.include_router(profesores_router, prefix="/profesores")
app.include_router(cursos_router, prefix="/cursos")
app.include_router(estudios_router, prefix="/generar_descuentos")
app.include_router(grupos_router, prefix="/grupos")

#################### MAIN #################

@app.get("/", tags=["main"])
def main():
    return RedirectResponse(url="/docs")
