"""Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности. """

import timeit
from collections import deque


def create_simle_lst():
    simple_lst = list(range(20))
    return simple_lst


def create_deque_lst():
    lst_deque = deque(range(20))
    return lst_deque


def add_to_simple_lst(s):
    s.append(5)
    return s


def add_to_deque_lst(d):
    d.append(5)
    return d


def rotate_simple_lst(s):
    s.append(s.pop(0))
    s.append(s.pop(0))
    return s


def rotate_deque_lst(d):
    d.rotate(-2)
    return d


def del_el_simple_lst(s):
    return s.pop()


def del_el_deque_lst(d):
    return d.pop()


def get_el_simple_lst(s):
    return s[10]


def get_el_deque_lst(d):
    return d[10]


print(
    f'Создание простого списка: {timeit.timeit("create_simle_lst()", "from __main__ import create_simle_lst", number=1000)}')
print(f'Создание очереди: {timeit.timeit("create_deque_lst()", "from __main__ import create_deque_lst", number=1000)}')

s = create_simle_lst()
# print(add_to_simple_lst(s))

d = create_deque_lst()
# print(add_to_deque_lst(d))

print(
    f'Добавление элемента в простой список: {timeit.timeit("add_to_simple_lst(s)", "from __main__ import add_to_simple_lst, s", number=1000)}')
print(
    f'Добавление элемента в конец очереди: {timeit.timeit("add_to_deque_lst(d)", "from __main__ import add_to_deque_lst, d", number=1000)}')

s2 = create_simle_lst()
# print(rotate_simple_lst(s2))

d2 = create_deque_lst()
# print(rotate_deque_lst(d2))

print(
    f'Перемещение 2-х первых элементов в конец простого списка: {timeit.timeit("rotate_simple_lst(s2)", "from __main__ import rotate_simple_lst, s2", number=1000)}')
print(
    f'Перемещение 2-х первых элементов в конец очереди: {timeit.timeit("rotate_deque_lst(d2)", "from __main__ import rotate_deque_lst, d2", number=1000)}')

s3 = create_simle_lst()
# print(del_el_simple_lst(s3))

d3 = create_deque_lst()
# print(del_el_deque_lst(d3))

print(
    f'Удаление последнего элемента с возвратом его значения в конце простого списка: {timeit.timeit("del_el_simple_lst(s3)", "from __main__ import del_el_simple_lst, s3", number=15)}')
print(
    f'Удаление последнего элемента с возвратом его значения в конце очереди: {timeit.timeit("del_el_deque_lst(d3)", "from __main__ import del_el_deque_lst, d3", number=15)}')

s4 = create_simle_lst()
# print(get_el_simple_lst(s4))

d4 = create_deque_lst()
# print(get_el_deque_lst(d4))

print(
    f'Получение 10-го элемента из простого списка: {timeit.timeit("get_el_simple_lst(s4)", "from __main__ import get_el_simple_lst, s4", number=1000)}')
print(
    f'Получение 10-го элемента из очереди: {timeit.timeit("get_el_deque_lst(d4)", "from __main__ import get_el_deque_lst, d4", number=1000)}')

"""
Создание простого списка: 0.001133000000000002
Создание очереди: 0.001979400000000006
Добавление элемента в простой список: 0.00047980000000000245
Добавление элемента в конец очереди: 0.00034029999999998783
Перемещение 2-х первых элементов в конец простого списка: 0.0015242000000000033
Перемещение 2-х первых элементов в конец очереди: 0.0006664000000000114
Удаление последнего элемента с возвратом его значения в конце простого списка: 1.3600000000002499e-05
Удаление последнего элемента с возвратом его значения в конце очереди: 7.399999999990747e-06
Получение 10-го элемента из простого списка: 0.0005123000000000072
Получение 10-го элемента из очереди: 0.0005742999999999998
"""

"""
Полученные замеры показали, что создание списка и получение элемента по индексу 
быстрее выполняются с использованием простых списков, а работа с добавлением, перемещением 
и удалением элементов с конца или начала - быстрее с использованием очереди deque
"""
