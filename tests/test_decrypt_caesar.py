import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import decrypt_caesar

def test_decrypt_caesar_uppercase_path():
    # Testa o caminho onde caracteres estão entre 'A' e 'Z'
    s = "ABC"
    shift = 1
    # 'A' -> 'Z', 'B' -> 'A', 'C' -> 'B'
    expected = "ZAB"
    result = decrypt_caesar(s, shift)
    assert result == expected

def test_decrypt_caesar_lowercase_path():
    # Testa o caminho onde caracteres estão entre 'a' e 'z'
    s = "abc"
    shift = 1
    # 'a' -> 'z', 'b' -> 'a', 'c' -> 'b'
    expected = "zab"
    result = decrypt_caesar(s, shift)
    assert result == expected

def test_decrypt_caesar_non_alpha_path():
    # Testa o caminho onde caracteres não estão entre 'A'-'Z' nem 'a'-'z'
    s = "A1!b"
    shift = 2
    # 'A' -> 'Z', '1' -> '1', '!' -> '!', 'b' -> 'z'
    expected = "Z1!z"
    result = decrypt_caesar(s, shift)
    assert result == expected