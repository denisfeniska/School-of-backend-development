def f(n):
    if n == 1:
        return 67353
    return f(n - 1) * ((240 * n + 400) / ((n * (39 * n + 89) * (3 * n + 2)) - (240 * n + 400)))


print(f(1046))