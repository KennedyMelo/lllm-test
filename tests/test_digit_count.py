import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import digit_count

def test_digit_count_zero_returns_one():
    result = digit_count(0)
    assert result == 1

def test_digit_count_non_zero_counts_digits():
    result = digit_count(12345)
    assert result == 5