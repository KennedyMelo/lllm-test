import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import palindrome_list

def test_palindrome_list_with_palindromic_strings():
    # Entrada com elementos que são palíndromos quando convertidos para string
    input_list = ['aba', 121, 'racecar', 12321]
    expected_output = ['aba', 121, 'racecar', 12321]
    result = palindrome_list(input_list)
    assert result == expected_output

def test_palindrome_list_with_non_palindromic_strings():
    # Entrada com elementos que não são palíndromos
    input_list = ['abc', 123, 'hello', 456]
    expected_output = []
    result = palindrome_list(input_list)
    assert result == expected_output