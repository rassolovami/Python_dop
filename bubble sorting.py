from random import randint

N = 10
arr = []
for i in range(N):
    arr.append(randint(1, 99))
print(arr)

for i in range(N - 1):
    for j in range(N - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Отсортированный массив:", arr)