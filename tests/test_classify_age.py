import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import classify_age

def test_classify_age_negative():
    result = classify_age(-5)
    assert result == 'inválido'

def test_classify_age_adult():
    result = classify_age(30)
    assert result == 'adulto'

def test_classify_age_minor():
    result = classify_age(10)
    assert result == 'menor'

def test_classify_age_senior():
    result = classify_age(70)
    assert result == 'idoso'