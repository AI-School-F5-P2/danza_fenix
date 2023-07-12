from pydantic import BaseModel
from typing import Optional

class RolValidator(BaseModel):
    nombre_rol: str
    
class UserValidator(BaseModel):
    login: str
    email: str
    password: str
    nombre_rol: str
    activo: Optional [int] = 1

