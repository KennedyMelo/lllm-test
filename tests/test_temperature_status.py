import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import temperature_status

def test_temperature_status_menor_ou_igual_a_0():
    result = temperature_status(-5)
    assert result == 'congelante'

def test_temperature_status_entre_0_e_20():
    result = temperature_status(10)
    assert result == 'frio'

def test_temperature_status_igual_a_20():
    result = temperature_status(20)
    assert result == 'agradável'

def test_temperature_status_entre_20_e_30():
    result = temperature_status(25)
    assert result == 'agradável'

def test_temperature_status_igual_a_30():
    result = temperature_status(30)
    assert result == 'quente'

def test_temperature_status_maior_que_30():
    result = temperature_status(35)
    assert result == 'quente'