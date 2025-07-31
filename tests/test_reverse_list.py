import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import reverse_list

def test_reverse_list_full_iteration_returns_reversed():
    input_list = [1, 2, 3]
    result = reverse_list(input_list)
    assert result == [3, 2, 1]

def test_reverse_list_empty_list_returns_empty():
    input_list = []
    result = reverse_list(input_list)
    assert result == []