import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import gcd

def test_gcd_b_zero_returns_a():
    # Caminho 1: b == 0, a qualquer valor
    a = 42
    b = 0
    result = gcd(a, b)
    assert result == a

def test_gcd_b_nonzero_enters_while_and_returns_a():
    # Caminho 2: b != 0, entra no loop while e retorna a
    a = 48
    b = 18
    result = gcd(a, b)
    # Como a função provavelmente implementa o algoritmo de Euclides,
    # o resultado esperado é o máximo divisor comum de 48 e 18, que é 6
    assert result == 6