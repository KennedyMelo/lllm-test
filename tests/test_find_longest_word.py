import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import find_longest_word

def test_find_longest_word_returns_none_for_falsy_input():
    # Testa o caminho onde 'words' é avaliado como falso (None, lista vazia, etc.)
    assert find_longest_word(None) is None
    assert find_longest_word([]) is None

def test_find_longest_word_returns_longest_after_loop():
    # Testa o caminho onde a função percorre a lista e retorna o maior valor
    words = ["a", "ab", "abc", "abcd"]
    result = find_longest_word(words)
    assert result == "abcd"