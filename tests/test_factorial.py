import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import factorial

def test_factorial_negative_input_returns_none():
    result = factorial(-5)
    assert result is None

def test_factorial_non_negative_input_computes_factorial():
    result = factorial(5)
    # 5! = 120
    assert result == 120