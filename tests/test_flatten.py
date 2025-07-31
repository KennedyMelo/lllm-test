import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import flatten

def test_flatten_with_nested_lists_returns_flat_list():
    # Entrada com uma lista de listas, deve percorrer ambos os loops e retornar uma lista achatada
    input_value = [[1, 2], [3, 4]]
    result = flatten(input_value)
    assert result == [1, 2, 3, 4]

def test_flatten_with_non_list_input_returns_empty():
    # Como o código percorre cada elemento de lst, se lst não for uma lista, o loop não executa
    # e result permanece vazio, retornando uma lista vazia
    input_value = "not a list"
    result = flatten(input_value)
    assert result == []