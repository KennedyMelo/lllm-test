import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import lcm

def test_lcm_returns_zero_when_a_is_zero():
    result = lcm(0, 5)
    assert result == 0

def test_lcm_returns_zero_when_b_is_zero():
    result = lcm(7, 0)
    assert result == 0

def test_lcm_swaps_values_when_a_less_than_b():
    # Aqui, a < b, então a troca deve ocorrer
    a = 3
    b = 10
    # Como não temos a implementação exata, assumimos que a função retorna um valor de LCM
    # Para testar, podemos calcular o LCM esperado manualmente
    # O LCM de 3 e 10 é 30
    result = lcm(a, b)
    assert result == 30
    # Além disso, podemos verificar que a troca ocorreu indiretamente, se necessário
    # Mas como a função não retorna os valores trocados, apenas verificamos o resultado esperado