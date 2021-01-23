from sqlalchemy import Column, Integer, String, ForeignKey

from .declarative_base import Base


class Interprete(Base):
    __tablename__ = 'interprete'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    texto_curiosidades = Column(String)
    cancion = Column(Integer, ForeignKey('cancion.id'))
