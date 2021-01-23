from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Cancion(Base):
    __tablename__ = 'cancion'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    minutos = Column(Integer)
    segundos = Column(Integer)
    compositor = Column(String)
    albumes = relationship('Album', secondary='album_cancion')
    interpretes = relationship('Interprete', cascade='all, delete, delete-orphan')


class AlbumCancion(Base):
    __tablename__ = 'album_cancion'

    cancion_id = Column(
        Integer,
        ForeignKey('cancion.id'),
        primary_key=True)

    album_id = Column(
        Integer,
        ForeignKey('album.id'),
        primary_key=True)
