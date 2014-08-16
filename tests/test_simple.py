import unittest
import buscacep


class ClientTests(unittest.TestCase):

    def test_busca_por_numero(self):
        cep = buscacep.busca("13820000")[0]
        self.assertEquals(cep.numero, "13820-000")

    def test_por_logradouro(self):
        ceps = buscacep.busca("Camata")
        print ceps
