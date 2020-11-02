import hashlib


def check_password(func):
    def get_result(n_d={}, passwd=''):
        passwd = input("Введите пароль: ")
        print(f'В базе данных хранится строка: {hashlib.sha256(log.encode() + passwd.encode()).hexdigest()}')
        n_d = func(log)
        if n_d.get(log) != hashlib.sha256(log.encode() + passwd.encode()).hexdigest():
            print(f'Вы ввели неверный пароль')
        else:
            print(f'Доступ разрешен')

    return get_result


@check_password
def creat_new_dict(log):
    passwd = input("Введите еще раз пароль: ")
    new_dict = {}

    new_dict[log] = hashlib.sha256(log.encode() + passwd.encode()).hexdigest()

    print(new_dict)

    return new_dict


log = input("Введите логин: ")
creat_new_dict(log)
