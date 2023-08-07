# from itertools import permutations
# from math import factorial

# def middle_permutation(string):
#   perm = permutations(sorted(string))
#   # print(type(perm))
#   middle_perm = list(perm)[factorial(len(string)) // 2 - 1]
#   return ''.join(map(str, middle_perm))

# print(middle_permutation("cba"))


from math import factorial


def middle_permutation(s: str) -> str:
    s = ''.join(sorted(s))
    n = len(s)
    mid = factorial(n) // 2 - 1
    result = []
    while n > 0:
        n -= 1
        index, mid = divmod(mid, factorial(n))
        result.append(s[index])
        s = s[:index] + s[index+1:]
    return ''.join(result)

