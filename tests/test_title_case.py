import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import title_case

def test_title_case_with_list_of_strings():
    input_value = ["hello", "world"]
    result = title_case(input_value)
    assert result == "Hello World"

def test_title_case_with_non_iterable_input():
    input_value = 123
    result = title_case(input_value)
    assert result == "123"