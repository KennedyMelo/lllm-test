import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import filter_odd

def test_filter_odd_returns_filtered_list_for_odd_elements():
    input_list = [1, 2, 3, 4, 5]
    result = filter_odd(input_list)
    assert result == [1, 3, 5]

def test_filter_odd_returns_empty_list_for_no_odd_elements():
    input_list = [2, 4, 6, 8]
    result = filter_odd(input_list)
    assert result == []