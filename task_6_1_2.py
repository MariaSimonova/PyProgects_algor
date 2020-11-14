from pympler import asizeof


class MyClass:
    __slots__ = ('p_1', 'p_2')

    def __init__(self, p_1, p_2):
        self.p_1 = p_1
        self.p_2 = p_2

    def __str__(self):
        return f'{self.p_1, self.p_2}'

    def __add__(self, other):
        return MyClass(self.p_1 + other.p_1, self.p_2 + other.p_2)

    def __mul__(self, other):
        return MyClass(self.p_1 * other.p_1, self.p_2 * other.p_2)


param_1 = MyClass(33, 44)
param_2 = MyClass(73, 84)
print(f'Сумма первого и второго элементов: {param_1 + param_2}')
print(f'Произведение первого и второго элементов: {param_1 * param_2}')

print(asizeof.asizeof(param_1))
print(asizeof.asizeof(param_2))

"""
Версия Python: 3.8
ОС: 64-разрядная версия

Результат загрузки памяти при использовании обычного класса:
328
328

Результат загрузки памяти при использовании класса со слотами:
112
112

Полученный результат в 2 раза меньше, так как был изменен вид хранения атрибутов класса 
со словаря (данный вид используется по умолчанию при использовании обычных классов 
и тебует больше объема памяти, так как является хеш-таблицей) на кортеж.
"""
