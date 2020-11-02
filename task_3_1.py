import time


def check_time(func):
    def g(n):
        start = time.time()
        func(n)
        end = time.time()
        return end - start

    return g


@check_time
def my_list(n):
    my_list = []

    for i in range(n):
        my_list.append(i)

    return my_list


@check_time
def my_dict(n):
    my_dict = {}

    for i in range(n):
        my_dict[i] = i

    return my_dict


print(f'Время выполнения заполнения списка: {my_list(1000000)}')
print(f'Время выполнения заполнения словоря: {my_dict(1000000)}')

"""Заполнение списка происходит быстрее, так как на заполенение словаря требуется больше времени
в связи с созданием (вычислением) хеший для ключей и решения коллизий
Время выполнения заполнения списка: 0.23885393142700195
Время выполнения заполнения словоря: 0.24684762954711914"""
