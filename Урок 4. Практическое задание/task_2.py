"""
Подсказка: примените мемоизацию
Добавьте аналитику: что вы сделали и почему
"""
import timeit

NUMBER = 123456789876543212345678987654321234567898765432198765432198765432165657474838392920101


def recursive_reverse(number):  # исходная программа возвращала лишний ноль, поправил ниже
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def other_reverse(number):  # норм версия исходной программы
    if number == 0:
        return ''
    return f'{str(number % 10)}{other_reverse(number // 10)}'


def new_reverse(number):  # быстрее, потому что ничего не приходится считать вообще, но без мемориизации
    return str(number)[::-1]


def cycles_reverse(number):  # быстрее, потому что цикл быстрее рекурсии, но тоже без меморизации
    reversed_digits = ''
    while number != 0:
        reversed_digits += str(number % 10)
        number = number // 10
    return reversed_digits


# вариант с меморизацией ниже, он быстр, но new_reverse быстрее и думать пришлось меньше, было очень интересно
CASH = {}


def memorization_reverse(number):
    numbers_list = list(str(number))
    reverse_list = []

    def rev(n):
        return n % 10

    for digit in numbers_list:
        if digit in CASH.keys():
            reverse_list.insert(0, CASH[digit])
        else:
            CASH[digit] = str(rev(int(digit)))
            reverse_list.insert(0, CASH[digit])
    return ''.join(reverse_list)


print(recursive_reverse(NUMBER))  # видно, что в конце есть лишний ноль
print(other_reverse(NUMBER))
print(new_reverse(NUMBER))
print(cycles_reverse(NUMBER))
print(memorization_reverse(NUMBER))
print(timeit.timeit(f'other_reverse({NUMBER})', setup='from __main__ import other_reverse', number=1))
print(timeit.timeit(f'new_reverse({NUMBER})', setup='from __main__ import new_reverse', number=1))
print(timeit.timeit(f'cycles_reverse({NUMBER})', setup='from __main__ import cycles_reverse', number=1))
print(timeit.timeit(f'memorization_reverse({NUMBER})', setup='from __main__ import memorization_reverse', number=1))
