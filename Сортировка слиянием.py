# Сортировка слиянием

def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

array = [5, 2, 8, 12, 1, 6]
sorted_array = merge_sort(array)
print(sorted_array)

# Тест
def test_merge_sort():
    array = [5, 2, 8, 12, 1, 6]
    sorted_array = merge_sort(array)
    assert sorted_array == [1, 2, 5, 6, 8, 12]

    array = [10, 5, 2, 8, 1, 3]
    sorted_array = merge_sort(array)
    assert sorted_array == [1, 2, 3, 5, 8, 10]

    array = [3, 2, 1]
    sorted_array = merge_sort(array)
    assert sorted_array == [1, 2, 3]

    array = []
    sorted_array = merge_sort(array)
    assert sorted_array == []

    print("Все тесты пройдены успешно!")

test_merge_sort()