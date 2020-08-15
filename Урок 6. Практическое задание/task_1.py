"""
Была взята 4 задача из 4 домашнего задания
Python 3.7.7
Windows 10 64bit
!!! ОЧЕНЬ СТРАННО !!! при импортировании рандомного модуля вторая функция перестает использовать память вообще!
"""
# import random
import memory_profiler

MY_ARR = [1, 3, 1, 3, 4, 5, 1, 4, 1, 3, 2, 8, 9, 1, 7, 1, 5, 1, 3, 3, 3, 3, 3, 3]

'''
При использовании списка ниже вместо верхнего, 3 функция показывает самое большое использование памяти, думаю это
связано с тем, что при большом количестве входных данных, функция хранит две большие коллекции (список и множество),
хотя почему при небольших входных данных она не затрачивает память мне непонятно...
В зависимости от количества входных данных, можно выбрать либо вторую либо третью функцию для минимизации затрат памяти,
так как первая всегда показывает большие затраты.
'''


# MY_ARR = [random.randint(0, 1000000) for i in range(1000)]

def memory_using(func):
    m1 = memory_profiler.memory_usage()
    func()
    m2 = memory_profiler.memory_usage()
    print(f'потрачено памяти: {m2[0] - m1[0]} MiB')


@memory_using
def func_1():
    m = 0
    num = 0
    for i in MY_ARR:
        count = MY_ARR.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@memory_using
def func_2():
    new_array = []
    for el in MY_ARR:
        count2 = MY_ARR.count(el)
        new_array.append(count2)
    max_2 = max(new_array)
    elem = MY_ARR[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


@memory_using
def func_3():
    count = 0
    for el in set(MY_ARR):
        if MY_ARR.count(el) > count:
            count = MY_ARR.count(el)
            max_elem = el
    return f'Чаще всего встречается число {max_elem}, ' \
           f'оно появилось в массиве {count} раз(а)'
