# importamos las librerias necesarias
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import db_host, db_port, db_name, db_user, db_password
# instanciamos el motor de base de datos

try:
    # creamos la conexion a la base de datos
    DATABASE_URL = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    # creamos la conexion a la base de datos
    engine = create_engine(DATABASE_URL)

    # creamos la sesion de la base de datos
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base = declarative_base() 
except Exception as e:
    raise ("Error al conectar a la base de datos")