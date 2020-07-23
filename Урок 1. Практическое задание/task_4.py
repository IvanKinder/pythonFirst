users = {'user1': ['pass', False], 'user2': ['password', True],
         'user3': ['password', True], 'user4': ['pass', False],
         'user5': ['pass', False], 'user6': ['password', True],
         'user7': ['password', True], 'user8': ['pass', False]}


def password_checker1(username):  # O(n)
    if username in users.keys():
        if users[username][1]:
            print('Пользователь может быть допущен к ресурсу!\n')
        else:
            pas = input('Введите пароль: ')
            if pas == users[username][0]:
                users[username][1] = True
                print('Пользователь может быть допущен к ресурсу!\n')
            else:
                print('Неверный пароль!\n')
    else:
        print('Такого пользователя несуществует!')


def password_checker2(username):  # O(3) - 'эффективнее, потому что меньше сложность
    try:
        if users[username][1]:
            print('Пользователь может быть допущен к ресурсу!\n')
        else:
            try:
                if input('Введите пароль: ') == users[username][0]:
                    users[username][1] = True
                    password_checker2(username)
                else:
                    raise Exception('Неверный пароль!\n')
            except Exception as e:  # pylint ругается, не понял, как исправить
                print(e)
    except KeyError:
        print('Такого пользователя не существует!\n')


while True:
    print('Input q to exit!')
    user = input('Введите имя пользователя: ')
    if user.lower() != 'q':
        password_checker2(user)
    else:
        print('\nВы вышли из программы!')
        break
