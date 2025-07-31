import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import sum_even_index

def test_sum_even_index_enters_loop_and_returns_total():
    # Teste com uma lista que faz o loop e retorna o total após a iteração
    lst = [1, 2, 3]
    result = sum_even_index(lst)
    # Como o loop percorre todos os elementos e soma todos, o resultado deve ser a soma de todos
    assert result == sum(lst)

def test_sum_even_index_sums_only_even_indices():
    # Teste com uma lista onde apenas índices pares são somados
    lst = [10, 5, 20, 7, 30]
    result = sum_even_index(lst)
    # Soma apenas elementos nos índices 0, 2, 4: 10 + 20 + 30 = 60
    assert result == 60