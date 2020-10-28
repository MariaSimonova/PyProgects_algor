def input_data():
    oper = input("Введите операцию (+, -, *, / или 0 для выхода): ")
    while True:
        if oper != "+" and oper != "-" and oper != "/" and oper != "*" and oper != "0":
            oper = input("Вы ввели неверно операцию. Введите операцию (+, -, *, / или 0 для выхода): ")
        else:
            break
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    while True:
        if b == 0:
            b = int(input("Второе число НЕ может быть 0. Введите второе число: "))
        else:
            break

    return oper, a, b


def operations():
    oper, a, b = input_data()

    if oper == "0":
        print(f'Процесс окончен')
    else:
        if oper == "+":
            print(f'Ваш результат: {a + b}')
            operations()
        elif oper == "-":
            print(f'Ваш результат: {a - b}')
            operations()
        elif oper == "*":
            print(f'Ваш результат: {a * b}')
            operations()
        else:
            print(f'Ваш результат: {a / b}')
            operations()


operations()
