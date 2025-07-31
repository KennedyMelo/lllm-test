import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import parity

def test_parity_even_number():
    # Testa o caminho onde n é par, esperando retornar 'par'
    n = 4
    result = parity(n)
    assert result == 'par'

def test_parity_odd_number():
    # Testa o caminho onde n é ímpar, esperando retornar 'ímpar'
    n = 3
    result = parity(n)
    assert result == 'ímpar'