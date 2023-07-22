from sqlalchemy import func
from datetime import datetime
from connection.connection import * 
from classes.models import Profesor
from fastapi.responses import JSONResponse

def qw_get_profesores():
    try:
        profesores = session.query(Profesor).all()
        if len(profesores) == 0:
<<<<<<< HEAD
            return "No hay datos"
        return profesores    
=======
            return JSONResponse(content={"message": "Error: El profesor/a especificado no existe."}, status_code=404)
        
>>>>>>> 015b98ac494e577d03dd6bc68573e4742f48fda8
    except Exception as e:
        return JSONResponse(content={"message": f"No se ha encontrar el profesor/a.{e}"}, status_code=400)
    return JSONResponse(content={"message": "El profesor/a ha sido Encontrado"}, status_code=202)


def qw_list_profesores():
    try:            
        profesores = session.query(Profesor).all()
        if len(profesores) == 0:
            return JSONResponse(content={"message": "Error: El profesor/a especificado no existe."}, status_code=404)
    except Exception as e:
        return JSONResponse(content={"message": f"No se ha podido borrar el profesor/a.{e}"}, status_code=400)
    return JSONResponse(content={"message": "El profesor/a ha sido borrado."}, status_code=202)


def qw_post_profesores(datos_profesor):
    try:
        profesor = Profesor(**datos_profesor)
        profesor_existe = session.query(Profesor).filter(Profesor.nombre_profesor == profesor.nombre_profesor).first()
        if profesor_existe is not None:
            return JSONResponse(content={"message": "El profesor/a ya existe."}, status_code=404)
        session.add(profesor)
        session.flush()
        session.commit()    
    except Exception as e:
        return JSONResponse(content={"message": f"El profesor no ha podido ser grabado.{e}"}, status_code=400)
    return JSONResponse(content={"message": "El profesor/a ha sido grabado."}, status_code=202)
    


def qw_put_profesores(nombre_profesor, nuevo_profesor):
    try:
        profesor = session.query(Profesor).filter(Profesor.nombre_profesor == nombre_profesor).first()
        if profesor is None:
<<<<<<< HEAD
            return "Profesor no existe"
        profesor.nombre_profesor = nuevo_profesor
        session.commit()
    except Exception as e: 
        return f"Error al modificar profesor/a. {e}"
    return "Profesor/a modificado."

=======
            return JSONResponse(content={"message": "Error: El profesor ya existe."}, status_code=404)
    except Exception as e:
        return JSONResponse(content={"message": f"No se ha podido añadir el profesor/a.{e}"}, status_code=400)
    return JSONResponse(content={"message": "El profesor/a ha sido añadir."}, status_code=202)

   
>>>>>>> 015b98ac494e577d03dd6bc68573e4742f48fda8
def qw_delete_profesores(borrar_profesor):
    try:
        profesor = session.query(Profesor).filter(Profesor.nombre_profesor == borrar_profesor).first()
        if profesor is None:
<<<<<<< HEAD
            return "Profesor no existe"    
        session.delete(profesor)
        session.commit()
    except Exception as e:
        return f"Error al eliminar profesor/a. {e}" 
    return "Profesor/a eliminado"
=======
            return JSONResponse(content={"message": "Error: El profesor especificado no existe."}, status_code=404)
        session.delete(profesor)
        session.commit()
  
    except Exception as e:
        return JSONResponse(content={"message": f"No se ha podido borrar el profesor/a.{e}"}, status_code=400)
    return JSONResponse(content={"message": "El profesor/a ha sido borrado."}, status_code=202)
>>>>>>> 015b98ac494e577d03dd6bc68573e4742f48fda8
