import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import distinct

def test_distinct_returns_empty_list_for_empty_input():
    # Caminho 1: lista vazia, result deve ser uma lista vazia
    result = distinct([])
    assert result == []

def test_distinct_adds_unique_elements_and_returns_result():
    # Caminho 2: lista com elementos, alguns repetidos
    input_list = [1, 2, 2, 3, 1]
    result = distinct(input_list)
    # Esperado: lista com elementos únicos na ordem de primeira ocorrência
    assert result == [1, 2, 3]
    # Garantir que todos os elementos do resultado estão na entrada
    for item in result:
        assert item in input_list
    # Garantir que o resultado não contém elementos repetidos
    assert len(result) == len(set(result))