from memory_profiler import profile


@profile
def check(n):
    def get_sum_2(lst_obj):
        if len(lst_obj) == 1:
            return lst_obj[0]
        else:
            return lst_obj[0] + get_sum_2(lst_obj[1:])

    return get_sum_2(n)


print(check(list(range(100))))

"""
Для того, чтобы получить результат полной картины по загрузке памяти при работе с
рекурсивными функциями, необходимо создать функцию-обертку, в рамках которой можно будет 
сделать суммарный замер по всем вызовам рекурсивной функции.
"""
