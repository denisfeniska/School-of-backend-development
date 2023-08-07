def last_digit(lst):
  if not lst:
    return 1
  else:
    n = 1
    for x in reversed(lst):
        n = x ** (n if n < 4 else n % 4 + 4)
    return n % 10
