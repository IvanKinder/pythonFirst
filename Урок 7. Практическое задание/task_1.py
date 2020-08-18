"""
Все равно не понимаю, почему после запуска первой функции счетчик памяти ломается всегда...
"""
from random import randint
from timeit import timeit
from memory_profiler import memory_usage

MY_MASS = [randint(-100, 100) for i in range(11)]
I_VAR = 'from __main__ import'
T_STR = 'Время выполнения'
M_STR = 'Потрачено памяти'


# MY_MASS = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def puz_sort(mass):
    for j in range(len(mass) - 1):
        for i in range(len(mass) - 1):
            if mass[i] < mass[i + 1]:
                a = mass[i]
                mass[i] = mass[i + 1]
                mass[i + 1] = a
    return mass


# Поскольку вероятность получить уже отсортированный массив при случайной генерации мала, придумал другую оптимизацию

def sort_optima(mass):
    for j in range(len(mass) - 1):
        for i in range(len(mass) - 1):
            if mass[i] < mass[i + 1]:
                a = mass[i]
                mass[i] = mass[i + 1]
                mass[i + 1] = a
            else:                       # добавленная строка
                break                   # добавленная строка
    return mass


# Ожидал, что на рандомном входящем массиве будет медленнее, чем второй, но нет,
# потому что мы выходим сразу из всех циклов и неважно первый прогон или нет

def sort_very_good(mass):
    flag = False                        # добавленная строка
    for j in range(len(mass) - 1):
        for i in range(len(mass) - 1):
            if mass[i] < mass[i + 1]:
                a = mass[i]
                mass[i] = mass[i + 1]
                mass[i + 1] = a
            else:
                flag = True             # добавленная строка
        if flag:                        # добавленная строка
            break                       # добавленная строка
    return mass


print(f'Исходный массив: {MY_MASS}')

m1 = memory_usage()
print(puz_sort(MY_MASS))
m2 = memory_usage()
print(f"{T_STR} без доработок: {timeit(f'puz_sort({MY_MASS})', setup=f'{I_VAR} puz_sort', number=1)}")
print(f'{M_STR} без доработок: {m2[0] - m1[0]} MiB')

m1 = memory_usage()
print(sort_optima(MY_MASS))
m2 = memory_usage()
print(f"{T_STR} с доработкой: {timeit(f'sort_optima({MY_MASS})', setup=f'{I_VAR} sort_optima', number=1)}")
print(f'{M_STR} с доработкой: {m2[0] - m1[0]} MiB')

m1 = memory_usage()
print(sort_very_good(MY_MASS))
m2 = memory_usage()
print(f"Лучшее {T_STR}: {timeit(f'sort_very_good({MY_MASS})', setup=f'{I_VAR} sort_very_good', number=1)}")
print(f'{M_STR} в самом быстром варианте: {m2[0] - m1[0]} MiB')
