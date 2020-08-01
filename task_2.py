two = 0
not_two = 0


def two_or_no(digit, two_count, not_two_count):
    if digit // 10 == 0:  # не понял, почему pilint ругается
        if digit % 2 == 0:
            two_count += 1
        else:
            not_two_count += 1
        return f'Чётных: {two_count}; нечётных: {not_two_count}'
    else:
        if digit % 2 == 0:
            two_count += 1
        else:
            not_two_count += 1
    return two_or_no(digit // 10, two_count, not_two_count)


try:
    print(two_or_no(int(input('Введите целое число: ')), two, not_two))
except ValueError:
    print('Надо вводить целые числа!!!\n')
