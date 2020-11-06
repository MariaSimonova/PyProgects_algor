"""
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# print(func_1([1, 2, 3, 4, 5, 6]))

nums = [1, 2, 3, 4, 5, 6]

print(timeit.timeit("func_1(nums)", setup="from __main__ import func_1, nums"))

"""Первоначальный вариант: 3.3748768"""


def p_even(nums):
    return [nums.index(x) for x in nums if x % 2 == 0]


n = [1, 2, 3, 4, 5, 6]

# print(p_even(nums))

print(timeit.timeit("p_even(n)", setup="from __main__ import p_even, n"))

"""Второй вариант: 2.6824566999999995. Результат улучшен с помощью 
ипользования comprehension"""
