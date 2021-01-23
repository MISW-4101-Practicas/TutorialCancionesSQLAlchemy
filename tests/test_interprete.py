import unittest

from src.logica.Coleccion import Coleccion
from src.modelo.interprete import Interprete
from src.modelo.declarative_base import Session


class InterpreteTestCase(unittest.TestCase):

    def setUp(self):
        self.session = Session()
        self.coleccion = Coleccion()

    def testAgregarInterprete(self):
        self.coleccion.agregarInterprete("Adele", "La artista tenia gripa..." , -1)
        self.consulta = self.session.query(Interprete).filter(Interprete.nombre == "Adele").first().nombre
        self.assertEqual(self.consulta, "Adele")

    def testEditarInterprete(self):
        self.coleccion.agregarInterprete("Lady Gaga", "Los trajes usados...", -1)
        self.consulta1 = self.session.query(Interprete).filter(Interprete.nombre == "Lady Gaga").first().id
        self.consulta2 = self.coleccion.editarInterprete(self.consulta1, "Lady Gaga", "Los trajes usados fueron elaborados...")
        self.assertTrue(self.consulta2)

    def testEliminarInterprete(self):
        self.coleccion.eliminarInterprete(1)
        self.consulta = self.session.query(Interprete).filter(Interprete.id == 1).first()
        self.assertIsNone(self.consulta)

    def testBuscarCancionesPorInterprete(self):
        self.consulta1 = self.session.query(Interprete).filter(Interprete.nombre == "Pipe Pelaez").first()
        if self.consulta1 is None:
            self.coleccion.agregarInterprete("Pipe Pelaez", "Primera canción vallenata...", -1)
            self.coleccion.agregarCancion("Tan natural", 2, 53, "Manuel Julian", -1,
                                          [{'id':'n', 'nombre': 'Pipe Pelaez', 'texto_curiosidades': 'Primera canción vallenata...'}])
        self.consulta2 = self.coleccion.buscarCancionesPorInterprete("pipe")
        self.assertEqual(len(self.consulta2), 1)

    def testBuscarInterpretesPorNombre(self):
        self.coleccion.agregarInterprete("Freddie Mercury", "Primera canción como solista", -1)
        self.coleccion.agregarInterprete("Freddy Burbano", "Canción que lo catapultó al éxito", -1)
        self.consulta = self.coleccion.buscarInterpretesPorNombre("fredd")
        self.assertEqual(len(self.consulta), 2)

    def testDarInterpretes(self):
        self.coleccion.agregarInterprete("Juan Gabriel", "Al finalizar el concierto en...", -1)
        self.consulta = self.coleccion.darInterpretes()
        self.assertGreater(len(self.consulta), 0)

    def testDarInterpretePorId(self):
        self.coleccion.agregarInterprete("Shakira", "La artista tenía el cabello color rojo", -1)
        self.interprete_id = self.session.query(Interprete).filter(Interprete.nombre == "Shakira").first().id
        self.consulta = self.coleccion.darInterpretePorId(self.interprete_id)["nombre"]
        self.assertEqual(self.consulta, "Shakira")
