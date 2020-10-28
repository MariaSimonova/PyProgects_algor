def input_oper():
    oper = input("Введите операцию (+, -, *, / или 0 для выхода): ")

    if oper == "+" or oper == "-" or oper == "/" or oper == "*" or oper == "0":
        return oper
    else:
        print(f'Операция введена неверно.')
        input_oper()

""""По функции input_numbers() ниже есть вопрос - пыталась также использовать рекурсию 
для получения значения отличного от нуля. Но она почему-то отдает значение b только один раз, если оно было 
введено один раз без повтороно выхова функции из самой себя,а если было введено b = 0, 
а потом после подсказки повторно любое другое значение, то после повторного вызова для b 
возвращается не введенное значение, None - не могу понять причину"""

def input_numbers():
    b = int(input("Введите второе число: "))

    if b != 0:
        return b
    else:
        print(f'Второе число НЕ может быть 0.')
        input_numbers()


def operations():
    oper = input_oper()

    if oper == "0":
        print(f'Процесс окончен')
    else:
        a = int(input("Введите первое число: "))
        b = input_numbers()
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


