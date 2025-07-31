import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import sum_odd_index

def test_sum_odd_index_returns_total_after_loop():
    # Testa o caminho 1: o loop percorre toda a lista e retorna total ao final
    lst = [10, 20, 30, 40]
    result = sum_odd_index(lst)
    # Os índices ímpares são 1 e 3, valores 20 e 40, total esperado 60
    assert result == 60

def test_sum_odd_index_sums_only_first_odd_index():
    # Testa o caminho 2: na primeira iteração, se i % 2 != 0, soma x a total e continua
    # Como a condição é verdadeira na primeira iteração, soma o elemento de índice 1
    lst = [5, 15, 25]
    result = sum_odd_index(lst)
    # Soma apenas o elemento na posição 1 (15), total esperado 15
    assert result == 15