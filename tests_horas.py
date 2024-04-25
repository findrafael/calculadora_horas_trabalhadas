import unittest
from horas import calcular_horas_trabalhadas

class TestCalcularHorasTrabalhadas(unittest.TestCase):
    def test_horas_trabalhadas_8(self):
        # Testa se 8 horas foram trabalhadas
        hora_entrada = "08:00"
        saida_almoco = "12:00"
        volta_almoco = "13:00"
        hora_saida = "17:00"
        horas_trabalhadas, atende_requisito = calcular_horas_trabalhadas(hora_entrada, saida_almoco, volta_almoco, hora_saida)
        self.assertEqual(horas_trabalhadas, 8)
        self.assertTrue(atende_requisito)

    def test_horas_trabalhadas_menos_de_8(self):
        # Testa se menos de 8 horas foram trabalhadas
        hora_entrada = "08:00"
        saida_almoco = "12:00"
        volta_almoco = "13:00"
        hora_saida = "16:30"
        horas_trabalhadas, atende_requisito = calcular_horas_trabalhadas(hora_entrada, saida_almoco, volta_almoco, hora_saida)
        self.assertLess(horas_trabalhadas, 8)
        self.assertFalse(atende_requisito)

    def test_horas_trabalhadas_mais_de_8(self):
        # Testa se mais de 8 horas foram trabalhadas
        hora_entrada = "08:00"
        saida_almoco = "12:00"
        volta_almoco = "13:00"
        hora_saida = "17:30"
        horas_trabalhadas, atende_requisito = calcular_horas_trabalhadas(hora_entrada, saida_almoco, volta_almoco, hora_saida)
        self.assertGreater(horas_trabalhadas, 8)
        self.assertTrue(atende_requisito)

if __name__ == '__main__':
    unittest.main()
