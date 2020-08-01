from random import randint

NUMBER_OF_TRY = 10
RAND_NUMBER = randint(0, 100)


def do_u_know(ran, max_count):
    print(f'Количество оставшихся попыток: {max_count}!')
    answer = input('Введите любое число от 0 до 100: ')
    try:
        if int(answer) == ran:
            print('Вы угадали!!!!!\n')
        else:
            if max_count == 1:
                print(f'Ваши попытки закончились! Загаданное число: {RAND_NUMBER}')
            else:
                if int(answer) > ran:
                    print('Ваше число больше, чем нужно!\n')
                if int(answer) < ran:
                    print('Ваше число меньше, чем нужно!\n')
                do_u_know(ran, max_count - 1)
    except ValueError:
        print('Надо вводить числа от 0 дод 100!!!!\n')
        do_u_know(ran, max_count)


do_u_know(RAND_NUMBER, NUMBER_OF_TRY)
