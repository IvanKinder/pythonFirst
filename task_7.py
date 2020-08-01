STEP = 1
PROGRESS_SUM = 0


def sum_progression_check(n, step, progression_sum):
    try:
        if int(n) == 1:
            return progression_sum + step
        else:
            progression_sum += step * int(n)
            return sum_progression_check(int(n) - 1, step, progression_sum)
    except RecursionError:
        return 'Вы ввели либо ноль, либо cлишком большое число...'


DIGITS_NUMBER = input('Введите натуральное число, при этом лучше не вводить больше 998: ')
try:
    print(sum_progression_check(DIGITS_NUMBER, STEP, PROGRESS_SUM))
    print(f'Проверка по формуле n(n+1)/2:\n{int(DIGITS_NUMBER) * (int(DIGITS_NUMBER) + 1) / 2}')
except ValueError:
    print('Не надо вводить символы и буквы!!!')
