import unittest
from assistente_virtual.core import executar_assistente

class TestAssistenteVirtual(unittest.TestCase):
    def test_executar_assistente(self):
        self.assertIsNone(executar_assistente())
