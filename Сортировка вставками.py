# Сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Тест сортировки вставками
arr = [5, 2, 9, 1, 7]
insertion_sort(arr)

print("Отсортированный массив:")
print(arr)