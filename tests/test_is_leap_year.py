import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import is_leap_year

def test_is_leap_year_divisible_by_400():
    # Caminho 1: year % 400 == 0, deve retornar True
    year = 2000
    result = is_leap_year(year)
    assert result is True

def test_is_leap_year_divisible_by_100_not_by_400():
    # Caminho 2: year % 400 != 0 e year % 100 == 0, deve retornar False
    year = 1900
    result = is_leap_year(year)
    assert result is False

def test_is_leap_year_divisible_by_4_not_by_100():
    # Caminho 3: year % 400 != 0, year % 100 != 0 e year % 4 == 0, deve retornar True
    year = 2016
    result = is_leap_year(year)
    assert result is True

def test_is_leap_year_not_divisible_by_4_or_100():
    # Caminho 4: year % 400 != 0, year % 100 != 0 e year % 4 != 0, deve retornar False
    year = 2019
    result = is_leap_year(year)
    assert result is False