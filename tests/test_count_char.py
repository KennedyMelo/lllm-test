import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import count_char

def test_count_char_iterates_and_counts_matching_char():
    s = "hello world"
    char = "l"
    result = count_char(s, char)
    # 'l' appears 3 times in "hello world"
    assert result == 3

def test_count_char_no_matching_char_returns_zero():
    s = "python"
    char = "z"
    result = count_char(s, char)
    # 'z' does not appear in "python"
    assert result == 0