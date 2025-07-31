import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import bubble_sort

def test_bubble_sort_com_lista_desordenada_retorna_lista_ordenada():
    # Entrada com lista desordenada
    input_list = [5, 3, 8, 1, 2]
    resultado = bubble_sort(input_list)
    # Esperado: lista ordenada
    assert resultado == [1, 2, 3, 5, 8]

def test_bubble_sort_lista_vazia_retorna_lista_vazia():
    # Entrada com lista vazia
    input_list = []
    resultado = bubble_sort(input_list)
    # Esperado: lista vazia
    assert resultado == []

def test_bubble_sort_lista_com_um_elemento_retorna_mesmo_elemento():
    # Entrada com lista de um elemento
    input_list = [42]
    resultado = bubble_sort(input_list)
    # Esperado: mesma lista
    assert resultado == [42]