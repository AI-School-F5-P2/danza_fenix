from fastapi import FastAPI
from starlette.responses import RedirectResponse
from apis.roles import router as roles_router
from apis.usuarios import router as usuarios_router
from apis.alumnos import router as alumnos_router 
from apis.niveles import router as niveles_router
from apis.profesores import router as profesores_router
from apis.cursos import router as cursos_router
from apis.compile import router as compile_router
from apis.grupos import router as grupos_router

tags_metadata = [
    {
        "name": "Roles",
        "description": "Operaciones con roles"
    },
    {
        "name": "Usuarios",
        "description": "Operaciones con usuarios"
    },
    {
        "name": "Alumnos",
        "description": "Operaciones de alumnos"
    },

    {
        "name": "Niveles",
        "description": "Operaciones con niveles"
    },
    {

        "name": "Profesores",
        "description" : "Operaciones con profesores"
    },
    {
        "name": "Cursos",
        "description": "Operaciones con cursos"
    },
    {
        "name": "Inscripcion",
        "description": "Operaciones con inscripciones"
    },
    {
        "name": "Grupos",
        "description": "Operaciones con grupos"
    }
]

app = FastAPI(openapi_tags=tags_metadata, description="API para la gestión de la escuela de danza Fenix")

# Registrar enrutadores
<<<<<<< HEAD
app.include_router(roles_router, prefix="/Roles")
app.include_router(usuarios_router, prefix="/Usuarios")
app.include_router(alumnos_router, prefix ="/Alumnos")
app.include_router(niveles_router, prefix = "/Niveles")
app.include_router(profesores_router, prefix="/Profesores")
app.include_router(cursos_router, prefix="/Cursos")
app.include_router(compile_router, prefix="/Compile")
app.include_router(grupos_router, prefix="/Grupos")
=======
app.include_router(roles_router, prefix="/roles")
app.include_router(usuarios_router, prefix="/usuarios")
app.include_router(alumnos_router, prefix ="/alumnos")

app.include_router(niveles_router, prefix = "/niveles")
app.include_router(profesores_router, prefix="/profesores")
app.include_router(cursos_router, prefix="/cursos")
app.include_router(compile_router, prefix="/generar_descuentos")
app.include_router(grupos_router, prefix="/grupos")
>>>>>>> 015b98ac494e577d03dd6bc68573e4742f48fda8

#################### MAIN #################

@app.get("/")
def main():
    return RedirectResponse(url="/docs")

