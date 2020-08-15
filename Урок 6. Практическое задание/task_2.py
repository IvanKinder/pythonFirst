import memory_profiler
from random import randint

'''Такое ощущение, что питон использует одну и ту же область памяти, созданную при вызове первой функции
 для всех функций, так что не могу с уверенностью сказать, какой из вариантов экономичнне, вероятно, одинаковые'''


def func_1():
    return [randint(0, 1000) for i in range(1000)]


def func_2():
    return tuple(randint(0, 1000) for i in range(1000))


def cycle_func():
    my_list = []
    for i in range(1000):
        my_list.append(randint(0, 1000))
    return my_list


m1 = memory_profiler.memory_usage()
for digit in func_1():
    print(digit, end=' ')
m2 = memory_profiler.memory_usage()
print(f'\nПервая функция: {m2[0] - m1[0]}')

m1 = memory_profiler.memory_usage()
for digit in func_2():
    print(digit, end=' ')
m2 = memory_profiler.memory_usage()
print(f'\nВторая функция: {m2[0] - m1[0]}')

m1 = memory_profiler.memory_usage()
for digit in cycle_func():
    print(digit, end=' ')
m2 = memory_profiler.memory_usage()
print(f'\nТретья функция: {m2[0] - m1[0]}')
