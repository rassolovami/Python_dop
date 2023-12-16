# Сортировка пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Тест сортировки пузырьком
arr = [5, 2, 9, 1, 7]
bubble_sort(arr)

print("Отсортированный массив:")
print(arr)