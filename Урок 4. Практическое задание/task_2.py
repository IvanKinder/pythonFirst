"""
Подсказка: примените мемоизацию
Добавьте аналитику: что вы сделали и почему
"""
import timeit
NUMBER = 123456789876543212345678987654321234567898765432198765432198765432165657474838392920101
def recursive_reverse(number):  # исходная программа возвращала лишний ноль, поправил
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

def other_reverse(number):  # норм версия исходной программы
    if number == 0:
        return ''
    return f'{str(number % 10)}{other_reverse(number // 10)}'

def new_reverse(number):  # быстрее, потому что ничего не приходится считать вообще, но без мемориизации
    return str(number)[::-1]

def memorization_reverse(number):  # быстрее, но тоже без меморизации
    reversed = []
    while number != 0:
        reversed.append(number % 10)
        number = number // 10

print(recursive_reverse(NUMBER))
print(other_reverse(NUMBER))
print(new_reverse(NUMBER))
print(memorization_reverse(NUMBER))
print(timeit.timeit(f'other_reverse({NUMBER})', setup='from __main__ import other_reverse', number=1))
print(timeit.timeit(f'new_reverse({NUMBER})', setup='from __main__ import new_reverse', number=1))
print(timeit.timeit(f'memorization_reverse({NUMBER})', setup='from __main__ import memorization_reverse', number=1))