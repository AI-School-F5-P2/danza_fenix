from fastapi.testclient import TestClient
from main import app
import time
import warnings


# para que no muestre informacion de deprecacion
warnings.filterwarnings("ignore", category=DeprecationWarning, module="sqlalchemy")

# from apis.cursos import router

client = TestClient(app=app)


#test main
def test_main():
    response = client.get("/") 
    assert response.status_code == 200


#test ruta get de todos los profesores 
def test_profesores():
    response = client.get("/Profesores/ver")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == [
  {
    "nombre_profesor": "Mar",
    "updated_at": "2023-07-13T18:01:54",
    "id": 1,
    "created_at": "2023-07-13T18:01:53"
  },
  {
    "nombre_profesor": "Flor",
    "updated_at": "2023-07-13T18:01:59",
    "id": 2,
    "created_at": "2023-07-13T18:01:59"
  },
  {
    "nombre_profesor": "Nayara",
    "updated_at": "2023-07-13T18:02:05",
    "id": 3,
    "created_at": "2023-07-13T18:02:04"
  },
  {
    "nombre_profesor": "Marifé",
    "updated_at": "2023-07-13T18:02:11",
    "id": 4,
    "created_at": "2023-07-13T18:02:10"
  },
  {
    "nombre_profesor": "Álvaro",
    "updated_at": "2023-07-13T18:02:16",
    "id": 5,
    "created_at": "2023-07-13T18:02:16"
  },
  {
    "nombre_profesor": "Nieves",
    "updated_at": "2023-07-13T18:02:26",
    "id": 6,
    "created_at": "2023-07-13T18:02:25"
  },
  {
    "nombre_profesor": "Sofía",
    "updated_at": "2023-07-13T18:02:33",
    "id": 7,
    "created_at": "2023-07-13T18:02:32"
  }
]
    

# test ruta get de un profesor
def test_profesor():
    response = client.get("/Profesores/busqueda_profesor?profesores=Mar")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == [
  {
    "nombre_profesor": "Mar",
    "updated_at": "2023-07-13T18:01:54",
    "created_at": "2023-07-13T18:01:53",
    "id": 1
  },
  {
    "nombre_profesor": "Marifé",
    "updated_at": "2023-07-13T18:02:11",
    "created_at": "2023-07-13T18:02:10",
    "id": 4
  }
]
    

#test  para la ruta de insertar profesores
def test_insertar_profesores():
    response = client.post("/Profesores/insertar", json={
    "nombre_profesor": "Luisa"
    })        

    assert response.status_code == 202
    assert response.headers["content-type"] == "application/json"
    assert response.json() == 	{"message": "El profesor/a ha sido grabado."}


#test  para la ruta de modificar profesores
def test_modificar_profesores():
    response = client.put("/Profesores/actualizar/Luisa/MariaDB", json={
    "nombre_profesor": "Luisa",
    "id": 8
    })        

    assert response.status_code == 202
    assert response.headers["content-type"] == "application/json"
    assert response.json() == 	{ "message": "El profesor/a ha sido actualizado."}


# test para la ruta de borrar profesores

def test_borrar_profesores():
    response = client.delete("/Profesores/eliminar/MariaDB")
    assert response.status_code == 202
    assert response.headers["content-type"] == "application/json"
    assert response.json() == 	{ "message": "El profesor/a ha sido borrado."}