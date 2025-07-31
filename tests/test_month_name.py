import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import month_name

def test_month_name_caminho_1():
    result = month_name(1)
    assert result == 'Janeiro'

def test_month_name_caminho_2():
    result = month_name(2)
    assert result == 'Fevereiro'

def test_month_name_caminho_3():
    result = month_name(3)
    assert result == 'Março'

def test_month_name_caminho_4():
    result = month_name(4)
    assert result == 'Abril'

def test_month_name_caminho_5():
    result = month_name(5)
    assert result == 'Maio'

def test_month_name_caminho_6():
    result = month_name(6)
    assert result == 'Junho'

def test_month_name_caminho_7():
    result = month_name(7)
    assert result == 'Julho'

def test_month_name_caminho_8():
    result = month_name(8)
    assert result == 'Agosto'

def test_month_name_caminho_9():
    result = month_name(9)
    assert result == 'Setembro'

def test_month_name_caminho_10():
    result = month_name(10)
    assert result == 'Outubro'

def test_month_name_caminho_11():
    result = month_name(11)
    assert result == 'Novembro'

def test_month_name_caminho_12():
    result = month_name(12)
    assert result == 'Dezembro'

def test_month_name_caminho_inválido():
    result = month_name(0)
    assert result == 'Inválido'