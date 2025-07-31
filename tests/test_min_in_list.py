import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import min_in_list

def test_min_in_list_empty_or_none_returns_none():
    # Caso em que lst é vazia
    result_vazio = min_in_list([])
    assert result_vazio is None

    # Caso em que lst é None
    result_none = min_in_list(None)
    assert result_none is None

def test_min_in_list_returns_min_value_after_iteration():
    # Lista com múltiplos elementos, incluindo valores negativos e positivos
    lst = [5, 3, 8, -2, 7]
    result = min_in_list(lst)
    # O menor valor na lista é -2
    assert result == -2

    # Lista com apenas um elemento
    single_element_list = [42]
    result_single = min_in_list(single_element_list)
    assert result_single == 42

    # Lista com todos elementos iguais
    equal_elements = [7, 7, 7]
    result_equal = min_in_list(equal_elements)
    assert result_equal == 7