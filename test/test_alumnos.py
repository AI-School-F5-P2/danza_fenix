from fastapi.testclient import TestClient
from main import app
import warnings
import pytest

warnings.filterwarnings("ignore", category=DeprecationWarning, module="sqlalchemy")

client = TestClient(app=app)


#test main
def test_main():
    response = client.get("/") 
    assert response.status_code == 200



#test ruta get de todos los alumnos
def test_alumnos():
    response = client.get("/Alumnos/mostrar_alumnos")
    assert response.status_code == 200
    



#test ruta get de alumno
def test_alumno():
    response = client.get("/Alumnos/mostrar_alumno100")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {
        "dni": "100",
        "nombre": "Alexa",
        "telefono": "0909",
        "descuento_familiar": 0,
        "apellidos": "tello",
        "email": "Ale@gmail.com",
        "updated_at": "2023-07-26 01:04:28",
        "nacimiento": "2023-07-25 18:44:28",
        "id": 3,
        "created_at": "2023-07-26 01:04:28",
        "created_at": "2023-07-26 01:04:28"
}




#test  para la ruta de insertar alumnos
def test_insertar_alumnos():
    response = client.post("/Alumnos/insertar", json={
    "nombre": "string",
    "apellidos": "string",
    "descuento_familiar": 0,
    "dni": "string",
    "email": "string",
     "telefono": "string",
    "nacimiento": "2023-07-25T16:47:50.160Z"

    })        

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == 	{"mensaje": "Alumno creado correctamente"}




#test  para la ruta de actualizar alumnos
def test_actualizar_alumnos():
    response = client.put("/Alumnos/actualizar_dni_alumno", json={
    "nombre": "string",
    "apellidos": "string",
    "descuento_familiar": 0,
    "dni": "string",
    "email": "string",
     "telefono": "string",
    "nacimiento": "2023-07-25T16:47:50.160Z"

    })        
    

def test_borrar_alumno():
    response = client.delete("/Alumnos/eliminar/100")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {'mensaje': 'Alumno eliminado correctamente'}
