"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import timeit
import random


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


orig_list = [round(random.random() * 50, 3) for _ in range(10)]

# замеры 10
print(orig_list)
print(merge_sort(orig_list))
print(timeit.timeit("merge_sort(orig_list[:])", setup="from __main__ import merge_sort, orig_list", number=1000))

orig_list_2 = [round(random.random() * 50, 3) for _ in range(100)]

# замеры 100
print(orig_list_2)
print(merge_sort(orig_list_2))
print(timeit.timeit("merge_sort(orig_list_2[:])", setup="from __main__ import merge_sort, orig_list_2", number=1000))

orig_list_3 = [round(random.random() * 50, 3) for _ in range(1000)]

# замеры 1000
print(orig_list_3)
print(merge_sort(orig_list_3))
print(timeit.timeit("merge_sort(orig_list_3[:])", setup="from __main__ import merge_sort, orig_list_3", number=1000))

"""
замеры 10  = 0.04588529999999999
замеры 100 = 0.5803561
замеры 1000 = 9.147162
"""
