import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataset.funcoes_ramificadas import binary_search

def test_binary_search_path_1_no_iterations():
    # low > high initially, loop skipped, should return None
    lst = [1, 2, 3]
    target = 0
    result = binary_search(lst, target)
    assert result is None

def test_binary_search_path_2_target_found():
    # target equals lst[mid], should return mid index
    lst = [1, 2, 3, 4, 5]
    target = 3
    result = binary_search(lst, target)
    assert result == 2

def test_binary_search_path_3_target_greater():
    # lst[mid] < target, low updated, loop continues
    lst = [1, 2, 4, 5]
    target = 5
    result = binary_search(lst, target)
    assert result == 3

def test_binary_search_path_4_target_smaller():
    # lst[mid] > target, high updated, loop continues
    lst = [1, 2, 4, 5]
    target = 2
    result = binary_search(lst, target)
    assert result == 1

def test_binary_search_path_5_target_not_found():
    # target not in list, loop ends, should return None
    lst = [1, 3, 5, 7]
    target = 4
    result = binary_search(lst, target)
    assert result is None