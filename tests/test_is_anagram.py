import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import is_anagram

def test_is_anagram_different_lengths_returns_false():
    s1 = "abc"
    s2 = "ab"
    result = is_anagram(s1, s2)
    assert result is False

def test_is_anagram_equal_lengths_returns_comparison_of_sorted_lists():
    s1 = "listen"
    s2 = "silent"
    result = is_anagram(s1, s2)
    expected = sorted(s1) == sorted(s2)
    assert result == expected