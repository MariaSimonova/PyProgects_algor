def reverse(n):
    l = list(n)

    if len(l) == 1:
        return l[0]
    else:
        return l.pop() + reverse(l)


n = input("Введите положительное число: ")
print(reverse(n))
