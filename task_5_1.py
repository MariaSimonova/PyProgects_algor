"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple

n = int(input("Введите количество предприятий для расчета прибыли: "))
companies = []
profits = []
companies_low = []
companies_above = []

while n >= 1:
    companies.append(input("Введите название предприятия: "))
    profits.append(sum([int(item) for item in input(
        "Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ").split()]))
    n -= 1

Marks = namedtuple('Marks', companies)
marks = Marks._make(profits)
print(marks)
print(f'Средняя годовая прибыль всех предприятий: {(marks[0] + marks[1]) / len(companies)}')

avarage_profit = (marks[0] + marks[1]) / len(companies)

for i in range(len(companies)):
    companies_above.append(companies[i]) if marks[i] > avarage_profit else companies_low.append(companies[i])

print(
    f'Предприятия, с прибылью выше среднего значения: {", ".join(companies_above)} \nПредприятия, с прибылью ниже среднего значения: {", ".join(companies_low)}')
