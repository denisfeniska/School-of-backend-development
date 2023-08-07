def max_sum_pair(arr, n):
    # Инициализация переменной с максимальной суммой и индексами пары
    max_sum = -1
    max_pair = []

    # Поиск максимальной суммы пары, кратной 112
    for i in range(n):
        for j in range(i+4, n):
            if (arr[i] > arr[j] and (arr[i] + arr[j]) % 112 == 0):
                if (arr[i] + arr[j]) > max_sum:
                    max_sum = arr[i] + arr[j]
                    max_pair = [arr[i], arr[j]]
    # Возвращаем максимальную сумму пары
    return max_sum


# Пример использования функции
N = int(input())
arr = []
for i in range(N):
  i = int(input())
  arr.append(i)
n = len(arr)

print(max_sum_pair(arr, n))
