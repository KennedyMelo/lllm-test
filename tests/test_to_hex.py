import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import to_hex

def test_to_hex_imediatamente_retorna_zero():
    # Caso em que n == 0, deve retornar '0' imediatamente
    resultado = to_hex(0)
    assert resultado == '0'

def test_to_hex_processa_numeros_positivos():
    # Caso em que n > 0, percorre o loop e retorna a string hexadecimal
    resultado = to_hex(255)
    # 255 em hexadecimal é 'ff'
    assert resultado == 'ff'