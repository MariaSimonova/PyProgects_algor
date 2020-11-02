"""Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв."""

import hashlib

s = input("Введите строку без пробелов, состоящую из латинских букв: ")
my_set = set()

for i in range(len(s)):
    for j in range(len(s), i, -1):
        if s[i:j] != s:
            my_set.add(hashlib.sha256(s[i:j].encode()).hexdigest())

print(my_set)
print(f'Количество уникальных подстрок: {len(my_set)}')
