"""Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число."""


def check_res(n):
    if n <= 0:
        return n
    else:
        return n + check_res(n - 1)


n = int(input("Введите положительное число: "))
res = int(n * (n + 1) / 2)

print(True if res == check_res(n) else False)
