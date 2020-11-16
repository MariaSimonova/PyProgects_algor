"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    flag = 0
    while True:
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = 1
        n += 1
        if n > len(lst_obj) or flag == 0:
            break
        else:
            continue

    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(orig_list)
print(bubble_sort(orig_list))
print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1))

orig_list_2 = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(orig_list_2)
print(bubble_sort(orig_list_2))
print(timeit.timeit("bubble_sort(orig_list_2)", setup="from __main__ import bubble_sort, orig_list_2", number=1))

orig_list_3 = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(orig_list_3)
print(bubble_sort(orig_list_3))
print(timeit.timeit("bubble_sort(orig_list_3)", setup="from __main__ import bubble_sort, orig_list_3", number=1))

"""
замеры 10  = 7.79999999999531e-06
замеры 100 = 2.539999999999487e-05
замеры 1000 = 0.00024970000000001935
"""
