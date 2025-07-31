import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import safe_divide

def test_safe_divide_b_zero_returns_none():
    a = 10
    b = 0
    result = safe_divide(a, b)
    assert result is None

def test_safe_divide_b_non_zero_returns_division():
    a = 10
    b = 2
    result = safe_divide(a, b)
    assert result == 5.0