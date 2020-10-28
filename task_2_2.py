def check_numbers(lst_obj):
    if len(lst_obj) == 1:
        return int(lst_obj[0]) % 2
    else:
        return int(lst_obj[0]) % 2 + check_numbers(lst_obj[1:])


n = input("Введите положительное число: ")
print(f'Количество четных чисел: {len(n) - check_numbers(n)}, Количество нечетных чисел: {check_numbers(n)}')
