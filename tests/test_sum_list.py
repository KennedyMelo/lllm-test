import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import sum_list

def test_sum_list_with_positive_numbers():
    # Caminho 1: soma de uma lista de números positivos
    lst = [1, 2, 3, 4]
    result = sum_list(lst)
    assert result == 10

def test_sum_list_with_empty_list():
    # Caminho 2: soma de uma lista vazia
    lst = []
    result = sum_list(lst)
    assert result == 0