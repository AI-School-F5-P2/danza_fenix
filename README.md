# Proyecto 2: API+SQL Danza Fénix

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Descripción del Proyecto

Este proyecto es parte de un trabajo de consultoría tecnológica para la escuela de baile Danza Fénix. El objetivo es desarrollar una solución para gestionar los alumnos y las clases de la escuela mediante una API REST y una base de datos SQL.

## Planteamiento

La dueña de Danza Fénix, Mar, necesita una forma más eficiente y digitalizada para gestionar los datos de los alumnos y las clases de su escuela de baile. Actualmente, todo se lleva a cabo en papel y bolígrafo, lo que resulta en un trabajo tedioso y propenso a errores. El objetivo es implementar una solución utilizando una base de datos SQL y una API REST para facilitar la gestión de los datos.

## Funcionalidades

- Gestión de alumnos: registro, actualización y eliminación de alumnos.
- Gestión de clases: creación, actualización y eliminación de clases.
- Cálculo de precios: aplicación de descuentos y precios según el tipo de clase y nivel.
- Relaciones entre alumnos y clases: un alumno puede estar inscrito en múltiples clases y viceversa.
- Gestión de profesores: asignación de profesores a las clases.

## Tecnologías Utilizadas

- Framework de desarrollo: [FastAPI](https://fastapi.tiangolo.com/)
- Base de datos: [PostgreSQL](https://www.postgresql.org/)
- ORM: [SQLAlchemy](https://www.sqlalchemy.org/)
- Herramienta de diagrama de base de datos: [dbdiagram.io](https://dbdiagram.io/)

## Requisitos de Instalación

- Python 3.7 o superior
- PostgreSQL 10 o superior
- Pipenv (opcional, pero recomendado)

## Instalación y Configuración

1. Clona el repositorio:

   ```bash
   git clone https://github.com/AI-School-F5-P2/danza_fenix.git


2.- crea un entorno virtual e instala los requirements.txt

    ```bash
    cd proyecto-danza-fenix
    python -m venv "fenix"  
    cd fenix/Scripts/ && ./activate

    pip install -r .\requirementes.txt  

3.- Configura la base de datos en el archivo :

    ```bash
    DATABASE_URL = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    crea un archivo config.py y rellan la sig informacion

    db_host = "localhost"
    db_port = "tu-puerto"
    db_name = "crudfastapi"
    db_user = "tu-usuario"
    db_password = "tu-contraseña"


4.- Ejecuta las migraciones de la base de datos:

    ```bash
    alembic upgrade head

5.- Inicia el servidor de desarrollo:

    ```bash    
    uvicorn app.main:app --reload
