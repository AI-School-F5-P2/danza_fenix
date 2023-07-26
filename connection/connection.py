from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes.models import Base

# Creamos la referencia al motor de base de datos
engine = create_engine('mysql+mysqlconnector://root:@localhost/danza_fenix', echo = True)
Base.metadata.create_all(bind=engine)

# Creamos la sesión para luego poder pasar las consultas.
Session = sessionmaker(bind = engine)
session = Session()
