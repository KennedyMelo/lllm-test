import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import days_in_month

def test_days_in_month_february_leap_true():
    result = days_in_month(2, leap=True)
    assert result == 29

def test_days_in_month_february_leap_false():
    result = days_in_month(2, leap=False)
    assert result == 28

def test_days_in_month_month_with_30_days():
    for month in [4, 6, 9, 11]:
        result = days_in_month(month)
        assert result == 30

def test_days_in_month_month_with_31_days():
    for month in [1, 3, 5, 7, 8, 10, 12]:
        result = days_in_month(month)
        assert result == 31

def test_days_in_month_unrecognized_month():
    result = days_in_month(13)
    assert result is None

def test_days_in_month_unrecognized_month_non_integer():
    result = days_in_month("abc")
    assert result is None