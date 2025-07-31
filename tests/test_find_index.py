import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import find_index

def test_find_index_value_found():
    lst = [10, 20, 30, 40]
    value = 30
    result = find_index(lst, value)
    assert result == 2

def test_find_index_value_not_found():
    lst = [1, 2, 3]
    value = 4
    result = find_index(lst, value)
    assert result == -1