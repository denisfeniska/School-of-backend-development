# from itertools import permutations


# def next_bigger(n):
#     # Преобразование числа в строку
#     n_str = str(n)
#     # Создание списка всех перестановок цифр числа n
#     perms = sorted(set(int(''.join(p)) for p in permutations(n_str)))
#     # Нахождение индекса числа n в списке perms
#     index = perms.index(n)
#     # Если число n является последним в списке perms, то возвращается -1
#     if index == len(perms) - 1:
#         return -1
#     # Иначе возвращается следующее число после n в списке perms
#     else:
#         return perms[index + 1]


def next_bigger(n):
    # Преобразование числа в строку
    n_str = str(n)
    # Создание списка цифр числа n
    digits = [int(d) for d in n_str]
    # Нахождение индекса первой цифры справа, которая меньше своей правой соседки
    for i in reversed(range(len(digits) - 1)):
        if digits[i] < digits[i + 1]:
            break
    else:
        # Если такой цифры нет, то возвращается -1
        return -1
    # Нахождение индекса наименьшей цифры справа от найденной ранее цифры, которая больше найденной ранее цифры
    for j in reversed(range(i + 1, len(digits))):
        if digits[j] > digits[i]:
            break
    # Обмен местами найденных ранее цифр
    digits[i], digits[j] = digits[j], digits[i]
    # Разворот части списка цифр справа от найденной ранее первой цифры
    digits[i + 1:] = reversed(digits[i + 1:])
    # Преобразование списка цифр обратно в число и возвращение результата
    return int(''.join(map(str, digits)))
