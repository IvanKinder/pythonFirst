"""
На очень большом количестве входных данных появляются цифры по памяти и как будто более быстрые варианты
почему-то требуют больше памяти, не уверен, что этому можно верить...
"""
from random import randint
from timeit import timeit
from memory_profiler import memory_usage

I_VAR = 'from __main__ import'
T_STR = 'Время выполнения'
M_STR = 'Потрачено памяти'

try:
    MY_MASS = [randint(-100, 100) for i in range(int(input('Введите количество элементов: ')))]


    # MY_MASS = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    def puz_sort(mass):
        for j in range(len(mass) - 1):
            for i in range(len(mass) - 1):
                if mass[i] < mass[i + 1]:
                    a = mass[i]
                    mass[i] = mass[i + 1]
                    mass[i + 1] = a
        return mass


    def sort_optima(mass):
        for j in range(len(mass) - 1):
            for i in range(len(mass) - 1):
                if mass[i] < mass[i + 1]:
                    a = mass[i]
                    mass[i] = mass[i + 1]
                    mass[i + 1] = a
                else:                           # добавленная строка
                    break                       # добавленная строка
        return mass


    # Ожидал, что на рандомном входящем массиве будет медленнее, чем второй, но нет,
    # потому что мы выходим сразу из всех циклов и неважно первый прогон или нет

    def sort_very_good(mass):
        flag = False                            # добавленная строка
        for j in range(len(mass) - 1):
            for i in range(len(mass) - 1):
                if mass[i] < mass[i + 1]:
                    a = mass[i]
                    mass[i] = mass[i + 1]
                    mass[i + 1] = a
                else:
                    flag = True                 # добавленная строка
            if flag:                            # добавленная строка
                break                           # добавленная строка
        return mass


    if __name__ == '__main__':
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

except ValueError:
    print('Необходимо ввести натуральное число!!!!!\n')
