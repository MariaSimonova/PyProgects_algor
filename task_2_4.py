def sum(n, res):
    if n <= 1:
        return res
    else:
        return res + sum(n - 1, res / -2)


n = int(input("Введите положительное число: "))
res = 1
print(sum(n, res))
