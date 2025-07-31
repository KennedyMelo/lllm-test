import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import encrypt_caesar

def test_encrypt_caesar_with_lowercase_letters_and_shift():
    s = "abcxyz"
    shift = 2
    result = encrypt_caesar(s, shift)
    # 'a' -> 'c', 'b' -> 'd', 'c' -> 'e', 'x' -> 'z', 'y' -> 'a', 'z' -> 'b'
    assert result == "cdezab"

def test_encrypt_caesar_with_non_lowercase_characters():
    s = "Hello, World! 123"
    shift = 3
    result = encrypt_caesar(s, shift)
    # Only lowercase letters between 'a' and 'z' are shifted; others remain unchanged
    # 'e' -> 'h', 'l' -> 'o', 'l' -> 'o', 'o' -> 'r'
    # 'r' -> 'u', 'd' -> 'g'
    # Non-lowercase characters stay the same
    expected = "Hello, World! 123"
    # Since the function only shifts lowercase letters, the expected output should be:
    # 'H' (not lowercase) stays, 'e' -> 'h', 'l' -> 'o', 'l' -> 'o', 'o' -> 'r'
    # 'W' (not lowercase) stays, 'o' -> 'r', 'r' -> 'u', 'l' -> 'o', 'd' -> 'g'
    # So the result should be: "Hhoor, Wruog! 123"
    expected_result = "Hhoor, Wruog! 123"
    assert result == expected_result