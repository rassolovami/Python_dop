# Сортировка выбором
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Тест сортировки выбором
arr = [5, 2, 9, 1, 7]
selection_sort(arr)

print("Отсортированный массив:")
print(arr)