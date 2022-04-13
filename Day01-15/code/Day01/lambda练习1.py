foo = [2, 18, 9, 22, None, 17, 24, 8, 12, 27]
new_list = filter(lambda x: (x is None) or (x % 3 == 0), foo)
print(list(new_list))

fg = lambda x: x + 1
print(fg(3))


def is_odd(n):
    return n % 2 == 1


newist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(*newist)
