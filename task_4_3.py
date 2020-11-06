"""
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit
import cProfile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def main():
    revers(num)
    revers_2(num)
    revers_3(num)


num = 11111111111111111111111122222222222222222222222222222222222222222222222222255555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555

print(timeit.timeit("revers(num)", setup="from __main__ import revers, num", number=1))
print(timeit.timeit("revers_2(num)", setup="from __main__ import revers_2, num", number=1))
print(timeit.timeit("revers_3(num)", setup="from __main__ import revers_3, num", number=1))

cProfile.run('main()')

"""
0.0019196999999999964
0.0013232999999999995
1.940000000000275e-05
"""

"""
426 function calls (7 primitive calls) in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
    420/1    0.003    0.000    0.003    0.003 task_4_3.py:13(revers)
        1    0.001    0.001    0.001    0.001 task_4_3.py:23(revers_2)
        1    0.000    0.000    0.000    0.000 task_4_3.py:31(revers_3)
        1    0.000    0.000    0.004    0.004 task_4_3.py:36(main)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

"""По итогам проведения профилировки времени выполнения функций можно сделат вывод, 
что функция revers самая длительная по времени выполнения, так как используется 
рекурсия, а самая быстрая - revers_3, так как вычисления основаны на использовании
встроенных функций. Результат в целом одинаковый и при использовании timeit и при cProfile"""
