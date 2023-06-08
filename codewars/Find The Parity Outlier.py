def find_outlier(integers):
    if integers[0] % 2 == 0:
        if integers[1] % 2 == 0:
            for i in integers:
                if i % 2 == 1:
                    return i
        elif integers[2] % 2 == 0:
            return integers[1]
        else:
            return integers[0]
    else:
        if integers[1] % 2 == 1:
            for i in integers:
                if i % 2 == 0:
                    return i
        elif integers[2] % 2 == 1:
            return integers[1]
        else:
            return integers[0]


print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
