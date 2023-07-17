# Proyecto Academia de danza Fénix

Este proyecto consiste en un sistema de gestión basado en API's para una academia de baile llamada Danza Fénix.
El acceso a los datos se realizará mediante API's a través de una interfaz de Swagger de la librería FastAPI, lo que lo hace especialmente útil para comunicarlo con otra aplicación, aunque lo limita pra su uso por parte de humanos.

### Estructura de archivos.
Los archivos y paquetes que componen la aplicación son los siguientes:
- **main.py**. Contiene la raíz del proyecto. Es desde donde arrancan todas las API's. No contiene API's de gestión de datos en sí mismo, sino importaciones de los archivos donde está dicha gestión.
- **/apis**. Este directorio contiene todos los archivos de API's que, a su vez, son importados en **main.py**.
- **/classes**. Contiene las clases más generales de la aplicación, como la de encriptación de contraseñas, las validaciones de Pydantic, la raíz de modelos, la raíz de consultas o los logs.
- **/conf**. Contiene archivos de configuración.
- **/connection**. Contiene la conexión a base de datos.
- **/models**. Contiene los archivos de modelos de las clases de las tablas.
- **/queries**. Contiene los archivos con las consultas para el CRUD de las distintas tablas.

### El CRUD de una tabla.
Cuando hay que crear el CRUD de una tabla debemos actuar sobre los siguientes puntos de la estructura de la aplicación:
- **/models**. Debemos asegurarnos de que exista el modelo de la tabla, tanto si es una tabla maestra como relacional.
- **/queries**. Debe existir un archivo con funciones especialmente diseñadas para todas las operaciones de CRUD sobre la tabla que nos interese.
- **/apis**. Debe existir un script con las API's que llaman a las fuunciones de **/queries**.
En los tres directorios mencionados se creará un archivo por cada CRUD, con el nombre de la tabla a la que se refiere dicho CRUD.

Además, para crear las API's de un CRUD hay que tocar los siguientes arcivos:
- **/classes/models.py**. Aquí importaremos el modelo de la tabla.
- **/classes/queries.py**. Aquí importaremos el archivo de consultas de la tabla.
- **/classes/validations.py**. Aquí incluimos los esquemas de tipos de datos de PyDantic relativos a la tabla con la que estamos trabajando.
- **main.py**. En este archivo se importa la API de cada tabla.
Estos cuatro archivos son comunes a todas las tablas, por lo que pueden dar problemas a la hora de mergear.


