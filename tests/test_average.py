import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import average

def test_average_returns_none_when_lst_is_none():
    result = average(None)
    assert result is None

def test_average_returns_none_when_lst_is_falsy():
    result = average([])
    assert result is None