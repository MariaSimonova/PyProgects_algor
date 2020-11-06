"""
Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""

import timeit


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num = 23

print(timeit.timeit("recursive_reverse(num)", setup="from __main__ import recursive_reverse, num"))

"""Первый вариант по вермени дольше и хуже из-за использования рекурсии: 2.750732"""


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r

    return g


@memorize
def recursive_reverse_2(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


n = 23

print(timeit.timeit("recursive_reverse_2(n)", setup="from __main__ import recursive_reverse_2, n"))

"""Второй вариант намного быстрее - оптимазация кода за счет получения данных из кэша, 
т.е. нет необходиммости в повторных вычислениях. Результат: 0.41902300000000015"""
