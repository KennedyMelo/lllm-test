import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import replace_char

def test_replace_char_replaces_matching_char():
    s = "hello world"
    old = "l"
    new = "x"
    result = replace_char(s, old, new)
    assert result == "hexxo worxd"

def test_replace_char_no_replacement_when_char_not_found():
    s = "python"
    old = "z"
    new = "x"
    result = replace_char(s, old, new)
    assert result == "python"