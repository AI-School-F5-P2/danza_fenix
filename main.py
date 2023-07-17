from fastapi import FastAPI
from starlette.responses import RedirectResponse
from apis.roles import router as roles_router
from apis.usuarios import router as usuarios_router
from apis.alumnos import router as alumnos_router 

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
    }
]

app = FastAPI(openapi_tags=tags_metadata)

# Registrar enrutadores
app.include_router(roles_router, prefix="/roles")
app.include_router(usuarios_router, prefix="/usuarios")
app.include_router(alumnos_router, prefix ="/alumnos")

#################### MAIN #################
@app.get("/", tags=["main"])
def main():
    return RedirectResponse(url="/docs")
