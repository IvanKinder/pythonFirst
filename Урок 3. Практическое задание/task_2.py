import hashlib

PASS_HASH_DATA = {}


def login_program():
    print('ДЛЯ ВЫХОДА ИЗ ПРОГРАММЫ ВВЕДИТЕ q!\n')
    user_name = input('Введите имя: ')
    if user_name.lower() == 'q':
        print('Вы вышли из программы!')
    else:
        if user_name in PASS_HASH_DATA.keys():
            user_pass = input('Пользователь существует! Введите пароль: ')
            full_pass = user_name + user_pass
            if hashlib.sha256(bytes(full_pass, encoding='utf-8')).hexdigest() == PASS_HASH_DATA[user_name].hexdigest():
                print('Пароль введен правильно!\n')
                login_program()
            else:
                print('Пароль введен неверно!!\n')
                login_program()
        else:
            user_pass = input('Новый пользователь! Введите пароль: ')
            PASS_HASH_DATA[user_name] = hashlib.sha256(bytes(user_name + user_pass, encoding='utf-8'))
            login_program()


login_program()
