"""Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш"""

import hashlib


class MemoryClass:
    def __init__(self):
        self.elems = []

    # создание хэша
    def make_hash(self, salt, elem):
        self.res = hashlib.sha256(salt.encode() + elem.encode()).hexdigest()
        return self.res

    # добавление url в кэш
    def add_elem(self, elem):
        if elem not in self.elems:
            self.elems.append(elem)

    # размер кэша
    def size(self):
        return len(self.elems)

    # состояние кэша
    def values(self):
        return self.elems


obj = MemoryClass()

# добавление url в кэш (используем ip-адрес сайта для "соли")
obj.add_elem(obj.make_hash("140.82.121.4", "https://github.com"))
obj.add_elem(obj.make_hash("140.82.121.4", "https://github.com"))
obj.add_elem(obj.make_hash("46.36.217.198", "https://python-scripts.com"))
obj.add_elem(obj.make_hash("46.36.217.198", "https://python-scripts.com"))

print(obj.size())  # количество элементов в кэш
print(obj.values())  # состояние кэша
