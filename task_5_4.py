"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import collections
import timeit


def create_regular_dict():
    regular_dict = {}
    regular_dict['a'] = 'A'
    regular_dict['b'] = 'B'
    regular_dict['c'] = 'C'
    regular_dict['d'] = 'D'
    regular_dict['e'] = 'E'
    return regular_dict


def create_ordered_dict():
    ordered_dict = collections.OrderedDict()
    ordered_dict['a'] = 'A'
    ordered_dict['b'] = 'B'
    ordered_dict['c'] = 'C'
    ordered_dict['d'] = 'D'
    ordered_dict['e'] = 'E'
    return ordered_dict


def iterate_regular_dict(rd):
    for k, v in rd.items():
        print(k, v)


def iterate_ordered_dict(od):
    for k, v in od.items():
        print(k, v)


def get_keys_regular_dict(rd):
    return rd.keys()


def get_keys_ordered_dict(od):
    return od.keys()


def get_value_regular_dict(rd):
    return rd.get('c')


def get_value_ordered_dict(od):
    return od.get('c')


def del_el_regular_dict(rd):
    return rd.popitem()


def del_el_ordered_dict(od):
    return od.popitem()


def add_el_regular_dict(rd):
    rd['f'] = 'F'
    return rd


def add_el_ordered_dict(od):
    od['f'] = 'F'
    return od


print(create_regular_dict())
print(create_ordered_dict())

print(
    f'Создание простого словаря: {timeit.timeit("create_regular_dict()", "from __main__ import create_regular_dict", number=1000)}')
print(
    f'Создание OrderedDict: {timeit.timeit("create_ordered_dict()", "from __main__ import create_ordered_dict", number=1000)}')

rd = create_regular_dict()
od = create_ordered_dict()

# iterate_regular_dict(rd)
# iterate_ordered_dict(od)

print(
    f'Перебор простого словаря: {timeit.timeit("iterate_regular_dict(rd)", "from __main__ import iterate_regular_dict, rd", number=100)}')
print(
    f'Перебор OrderedDict: {timeit.timeit("iterate_ordered_dict(od)", "from __main__ import iterate_ordered_dict, od", number=100)}')

rd2 = create_regular_dict()
od2 = create_ordered_dict()

# print(get_keys_regular_dict(rd2))
# print(get_keys_ordered_dict(od2))


print(
    f'Получение ключей простого словаря: {timeit.timeit("get_keys_regular_dict(rd2)", "from __main__ import get_keys_regular_dict, rd2", number=100)}')
print(
    f'Получение ключей OrderedDict: {timeit.timeit("get_keys_ordered_dict(od2)", "from __main__ import get_keys_ordered_dict, od2", number=100)}')

rd3 = create_regular_dict()
od3 = create_ordered_dict()

# print(get_value_regular_dict(rd3))
# print(get_value_ordered_dict(od3))

print(
    f'Получение значения по ключу из простого словаря: {timeit.timeit("get_value_regular_dict(rd3)", "from __main__ import get_value_regular_dict, rd3", number=100)}')
print(
    f'Получение значения по ключу из OrderedDict: {timeit.timeit("get_value_ordered_dict(od3)", "from __main__ import get_value_ordered_dict, od3", number=100)}')

rd4 = create_regular_dict()
od4 = create_ordered_dict()

# print(del_el_regular_dict(rd4))
# print(del_el_ordered_dict(od4))

print(
    f'Удаление последней пары из простого словаря: {timeit.timeit("del_el_regular_dict(rd4)", "from __main__ import del_el_regular_dict, rd4", number=2)}')
print(
    f'Удаление последней пары из OrderedDict: {timeit.timeit("del_el_ordered_dict(od4)", "from __main__ import del_el_ordered_dict, od4", number=2)}')

rd5 = create_regular_dict()
od5 = create_ordered_dict()

# print(add_el_regular_dict(rd5))
# print(add_el_ordered_dict(od5))

print(
    f'Добавление новой пары в простой словарь: {timeit.timeit("add_el_regular_dict(rd5)", "from __main__ import add_el_regular_dict, rd5", number=1000)}')
print(
    f'Добавление новой пары в OrderedDict: {timeit.timeit("add_el_ordered_dict(od5)", "from __main__ import add_el_ordered_dict, od5", number=1000)}')

"""
Создание простого словаря: 0.0006160000000000054
Создание OrderedDict: 0.0011884000000000061
Перебор простого словаря: 0.021235699999999996
Перебор OrderedDict: 0.022503600000000012
Получение ключей простого словаря: 3.3599999999994745e-05
Получение ключей OrderedDict: 3.3299999999999996e-05
Получение значения по ключу из простого словаря: 3.199999999999037e-05
Получение значения по ключу из OrderedDict: 3.350000000000575e-05
Удаление последней пары из простого словаря: 3.299999999997749e-06
Удаление последней пары из OrderedDict: 5.600000000008376e-06
Добавление новой пары в простой словарь: 0.0006141000000000063
Добавление новой пары в OrderedDict: 0.0009677999999999909
"""

"""
Согласно проведенным замерам работа с OrderedDict не является эффективной по 
крайней мере для версий Python выше 3.5, так как выполнение операций с использованием
OrderedDict требует больше времени, чем использование обычного словаря.
"""
