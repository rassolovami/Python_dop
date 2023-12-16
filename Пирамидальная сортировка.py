# Пирамидальная сортировка

def heapify(arr, n, i):
    largest = i  # Инициализация наибольшего элемента как корня
    l = 2 * i + 1     # Левый потомок
    r = 2 * i + 2     # Правый потомок
 
    # Проверяем, существует ли левый потомок и больше ли он корня
    if l < n and arr[i] < arr[l]:
        largest = l
 
    # Проверяем, существует ли правый потомок и больше ли он корня или левого потомка
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Если наибольший элемент не корень, то меняем местами с корнем
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # свап
 
        # Применяем heapify к поддереву
        heapify(arr, n, largest)
 
 
def heapSort(arr):
    n = len(arr)
 
    # Перестраиваем кучу (переупорядочиваем массив)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # Извлекаем элементы один за другим
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # свап
        heapify(arr, i, 0)
 
 
# Тест
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print("Отсортированный массив:")
for i in range(len(arr)):
    print("%d" % arr[i])