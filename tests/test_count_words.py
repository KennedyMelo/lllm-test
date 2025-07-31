import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import count_words

def test_count_words_empty_string_returns_zero():
    result = count_words("")
    assert result == 0

def test_count_words_spaces_only_returns_zero():
    result = count_words("     ")
    assert result == 0

def test_count_words_non_empty_string_returns_word_count():
    result = count_words("hello world this is a test")
    assert result == 6