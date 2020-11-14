"""
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
"""

from memory_profiler import profile, memory_usage


def p_even(nums):
    print([nums.index(x) for x in nums if x % 2 == 0])


mem1 = memory_usage()
p_even(list(range(10000)))
mem2 = memory_usage()

print(f"Загрузка {mem2[0] - mem1[0]} Mib")


def p_even_2(nums):
    for i in nums:
        if i % 2 == 0:
            yield i


m1 = memory_usage()
g = p_even_2(list(range(10000)))
for j in g:
    print(j)
m2 = memory_usage()

print(f"Загрузка памяти: {m2[0] - m1[0]} Mib")

"""
Версия Python: 3.8
ОС: 64-разрядная версия

В первом случае при использовании comprehention - Загрузка памяти: 0.3125 Mib
Во втором случае при использовании генератора - Загрузка памяти: 0.1875 Mib. 
Во втором случае результат практически в 2 раза меньше, так как при использовании 
генераторов не требуется хранение данных в памяти и все вычисления проводятся по запросу.
"""
