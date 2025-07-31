import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import contains

def test_contains_returns_true_when_value_found_in_list():
    lst = [1, 2, 3, 4]
    value = 3
    result = contains(lst, value)
    assert result is True

def test_contains_returns_false_when_value_not_in_list():
    lst = [1, 2, 3, 4]
    value = 5
    result = contains(lst, value)
    assert result is False