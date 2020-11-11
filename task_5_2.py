from collections import defaultdict


class MyClass:
    def __init__(self, p):
        self.p = p

    def my_func(self, p):
        for i in self.p:
            my_dict[self.p].append(i)
        return my_dict[self.p]

    def __str__(self):
        return hex(self.p)

    def __add__(self, other):
        return MyClass(int(self.p, 16) + int(other.p, 16))

    def __mul__(self, other):
        return MyClass(int(self.p, 16) * int(other.p, 16))


my_dict = defaultdict(list)
my_1 = MyClass(input("Введите первое число в шестнадцатиричном формате: "))
my_2 = MyClass(input("Введите второе число в шестнадцатиричном формате: "))
print(f'Первое шестнадцатиричное число: {my_1.my_func(my_1)}')
print(f'Второе шестнадцатиричное число: {my_2.my_func(my_2)}')

a = str(my_1 + my_2).upper()
my_3 = MyClass(a[2:])
b = str(my_1 * my_2).upper()
my_4 = MyClass(b[2:])
print(f'Сумма шестнадцатиричных чисел: {my_3.my_func(my_3)}')
print(f'Произведение шестнадцатиричных чисел: {my_4.my_func(my_4)}')


