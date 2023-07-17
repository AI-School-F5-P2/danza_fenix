from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime


class RolValidator(BaseModel):
    nombre_rol: str

class UserValidator(BaseModel):
    login: str
    email: str
    password: str
    nombre_rol: str
    activo: Optional [int] = 1


class AlumnoValidator(BaseModel):
    nombre: str
    apellidos: str
    descuento_familiar: int
    dni: str
    email: str
    telefono: str
    nacimiento: datetime


