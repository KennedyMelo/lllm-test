import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import sum_digits

def test_sum_digits_with_positive_integer():
    # Caminho 1: n é um inteiro positivo, soma dos dígitos
    result = sum_digits(123)
    assert result == 6  # 1 + 2 + 3 = 6

def test_sum_digits_with_negative_integer():
    # Caminho 2: n é um inteiro negativo, soma dos dígitos da representação absoluta
    result = sum_digits(-456)
    assert result == 15  # 4 + 5 + 6 = 15