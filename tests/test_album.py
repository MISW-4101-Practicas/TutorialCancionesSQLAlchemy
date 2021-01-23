import unittest

from src.logica.Coleccion import Coleccion
from src.modelo.album import Album
from src.modelo.declarative_base import Session


class AlbumTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.coleccion = Coleccion()

    def testAgregarAlbum(self):
        self.coleccion.agregarAlbum("Mio", 2000, "Sin descripción", "CD")
        self.coleccion.agregarAlbum("Clara luna", 1992, "Sin descripción", "CASETE")
        self.consulta1 = self.session.query(Album).filter(Album.titulo == "Mio").first()
        self.consulta2 = self.session.query(Album).filter(Album.id == 2).first()
        self.assertEqual(self.consulta1.titulo, "Mio")
        self.assertIsNotNone(self.consulta2)

    def testEditarAlbum(self):
        self.coleccion.editarAlbum(2, "Clara luna-Mix", 1982, "Sin descripción", "DISCO")
        self.consulta = self.session.query(Album).filter(Album.id == 2).first()
        self.assertIsNot(self.consulta.titulo, "Clara luna")

    def testEliminarAlbum(self):
        self.coleccion.eliminarAlbum(1)
        self.consulta = self.session.query(Album).filter(Album.id == 1).first()
        self.assertIsNone(self.consulta)

    def testBuscarAlbumesPorTitulo(self):
        self.consulta1 = self.coleccion.buscarAlbumesPorTitulo("clara luna")
        self.coleccion.agregarAlbum("Clara luna-Instrumental", 1992, "Sin descripción", "CD")
        self.consulta2 = self.coleccion.buscarAlbumesPorTitulo("clara luna")
        self.assertGreater(len(self.consulta2), len(self.consulta1))

    def testDarAlbumPorId(self):
        self.coleccion.agregarAlbum("Infinito arcoiris", 1990, "Sin descripción", "CASETE")
        self.album_id = self.session.query(Album).filter(Album.titulo == "Infinito arcoiris").first().id
        self.consulta = self.coleccion.darAlbumPorId(self.album_id)["titulo"]
        self.assertEqual(self.consulta, "Infinito arcoiris")

    def testDarAlbumes(self):
        self.consulta1 = self.coleccion.darAlbumes()
        self.coleccion.agregarAlbum("New life", 2018, "Album escrito para...", "CD")
        self.consulta2 = self.coleccion.darAlbumes()
        self.assertGreater(len(self.consulta2), len(self.consulta1))
