import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import find_first_upper

def test_find_first_upper_returns_first_upper_char():
    # Caminho 1: encontra a primeira letra maiúscula e retorna
    s = "aBcDe"
    result = find_first_upper(s)
    assert result == "B"

def test_find_first_upper_returns_none_when_no_upper():
    # Caminho 2: não há letras maiúsculas, retorna None
    s = "abcdef"
    result = find_first_upper(s)
    assert result is None
