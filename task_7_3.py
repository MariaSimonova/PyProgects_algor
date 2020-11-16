"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

import timeit
import random
from statistics import median


def find_median(lst_obj):
    def gnome(data):
        i, size = 1, len(data)
        while i < size:
            if data[i - 1] <= data[i]:
                i += 1
            else:
                data[i - 1], data[i] = data[i], data[i - 1]
                if i > 1:
                    i -= 1
        return data

    lst = gnome(lst_obj)
    return lst, lst[int((len(lst) - 1) / 2)]


def find_median_2(lst_obj):
    j = 0
    while True:
        left = []
        right = []
        m = lst_obj[j]

        for i in range(len(lst_obj)):
            if i == j:
                pass
            else:
                if lst_obj[i] <= m:
                    left.append(lst_obj[i])
                else:
                    right.append(lst_obj[i])

        if len(left) == len(right):
            break
        else:
            j += 1
            continue

    return m


def find_median_3(lst_obj):
    return median(lst_obj)


m = int(input("Введите натуральное число: "))
orig_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]

print(orig_list)
print(find_median(orig_list))
print(timeit.timeit("find_median(orig_list)", setup="from __main__ import find_median, orig_list", number=1))
print(find_median_2(orig_list))
print(timeit.timeit("find_median_2(orig_list)", setup="from __main__ import find_median_2, orig_list", number=1))
print(find_median_3(orig_list))
print(timeit.timeit("find_median_3(orig_list)", setup="from __main__ import find_median_3, orig_list", number=1))

"""
для m = 3, Медиана: -22 - для массива, указанного ниже:
[2, -23, 45, -97, -56, 8, -22]
([-97, -56, -23, -22, 2, 8, 45], -22)
Затраченное время с использованием сортровки Гномья: 8.999999999981245e-06
Затраченное время без сортировки: 2.0000000000020002e-05
Затраченное время с использованием встроенной функции median: 4.900000000002125e-06

Замеры показали, что самая медленная функция поиска медианы, - вторая (без сортировки),
а сама быстрая - третья (с использованием встроенной функции).
"""
