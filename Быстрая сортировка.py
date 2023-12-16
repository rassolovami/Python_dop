# Быстрая сортировка

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # выбираем опорный элемент
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quicksort(less) + equal + quicksort(greater)

# пример использования
arr = [5, 2, 8, 1, 9, 4]
sorted_arr = quicksort(arr)
print(sorted_arr)

import pytest
from quicksort import quicksort

def test_quicksort():
    arr = [5, 2, 8, 1, 9, 4]
    sorted_arr = quicksort(arr)
    assert sorted_arr == [1, 2, 4, 5, 8, 9]

    arr = [10, 5, 8, 2, 1]
    sorted_arr = quicksort(arr)
    assert sorted_arr == [1, 2, 5, 8, 10]

    arr = []
    sorted_arr = quicksort(arr)
    assert sorted_arr == []

    arr = [1]
    sorted_arr = quicksort(arr)
    assert sorted_arr == [1]

    arr = [3, 3, 3, 3]
    sorted_arr = quicksort(arr)
    assert sorted_arr == [3, 3, 3, 3]

pytest.main()