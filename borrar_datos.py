from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.album import Album, Medio
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    session = Session()
    cancion2 = session.query(Cancion).get(2)
    session.delete(cancion2)
    session.commit()
    session.close()

    """ En el ejemplo, y según la definición de las clases, se debe tener cuidado con el borrado de intérpretes, dado que, al no estar relacionados a través de la instrucción relationship, 
  es posible borrarlos y dejar las canciones con una relación a un intérprete inexistente. 
  Para profundizar en las relaciones se recomienda revisar esta referencia. """
