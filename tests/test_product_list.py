import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import product_list

def test_product_list_multiplica_elementos_caminho_1():
    # Testa o caminho onde a função multiplica todos os elementos de lst
    lst = [2, 3, 4]
    result = product_list(lst)
    assert result == 24  # 1*2*3*4 = 24

def test_product_list_multiplica_elementos_caminho_2():
    # Testa o caminho onde a função multiplica todos os elementos de lst
    lst = [5, 0, -1]
    result = product_list(lst)
    assert result == 0  # 1*5*0*(-1) = 0