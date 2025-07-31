import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import max_in_list

def test_max_in_list_empty_list_returns_none():
    result = max_in_list([])
    assert result is None

def test_max_in_list_non_empty_list_returns_max():
    result = max_in_list([1, 3, 2, 5, 4])
    assert result == 5