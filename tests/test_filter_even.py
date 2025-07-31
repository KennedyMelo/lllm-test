import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import filter_even

def test_filter_even_with_mixed_elements():
    # Caminho 1: lista com elementos pares e ímpares
    input_list = [1, 2, 3, 4, 5, 6]
    result = filter_even(input_list)
    assert result == [2, 4, 6]

def test_filter_even_with_empty_list():
    # Caminho 2: lista vazia
    input_list = []
    result = filter_even(input_list)
    assert result == []