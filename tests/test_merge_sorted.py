import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import merge_sorted

def test_merge_sorted_path_1():
    # Caminho 1: a condição do if dentro do while é verdadeira várias vezes
    a = [1, 3, 5]
    b = [2, 4, 6]
    # Para garantir que a condição do if seja verdadeira, podemos fazer a[0] < b[0]
    # e que a[0] seja menor que b[0], e que a[0] seja menor que b[0], etc.
    # Como a lógica de merge geralmente compara elementos, vamos usar esses valores
    resultado = merge_sorted(a, b)
    # Esperado: elementos de a e b intercalados em ordem
    assert resultado == [1, 2, 3, 4, 5, 6]

def test_merge_sorted_path_2():
    # Caminho 2: a condição do if dentro do while é falsa, entra no else
    a = [2, 4, 6]
    b = [1, 3, 5]
    # Aqui, a[0] >= b[0], então a condição do if será falsa inicialmente
    resultado = merge_sorted(a, b)
    # Esperado: elementos de b primeiro, depois de a
    assert resultado == [1, 2, 3, 4, 5, 6]

def test_merge_sorted_path_3():
    # Caminho 3: após o while, extendem-se os remanescentes de a e b
    a = [1, 2]
    b = [3, 4]
    # Aqui, a[0] < b[0], então o while processa até que a ou b acabem
    # Como a termina primeiro, o resultado deve incluir os elementos remanescentes de b
    resultado = merge_sorted(a, b)
    # Esperado: elementos de a e b em ordem
    assert resultado == [1, 2, 3, 4]