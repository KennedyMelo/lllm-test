import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import to_binary

def test_to_binary_zero_returns_string_zero():
    result = to_binary(0)
    assert result == '0'

def test_to_binary_positive_number_returns_binary_string():
    # Para um número maior que zero, por exemplo 5, que em binário é '101'
    result = to_binary(5)
    assert result == '101'