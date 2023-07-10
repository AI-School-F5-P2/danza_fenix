from pydantic import BaseModel
from typing import Optional

class RolValidator(BaseModel):
    nombre_rol: str