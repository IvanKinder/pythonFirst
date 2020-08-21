"""
С удовольствием придумал бы еще варианты без сортировки, но не успеваю =(
"""
from random import uniform
from statistics import median
from timeit import timeit


def without_sort(mas):  # С увеличением размера массива начинает иногда ошибаться
    middle_ari = sum([n for n in mas]) / len(mas)
    check_dict = {}
    for el in mas:
        check_dict[abs(el - middle_ari)] = el
    return check_dict[min(check_dict.keys())]


def with_sort(mas):
    def gnome(data):
        i, size = 1, len(data)
        while i < size:
            if data[i - 1] <= data[i]:
                i += 1
            else:
                data[i - 1], data[i] = data[i], data[i - 1]
                if i > 1:
                    i -= 1
        return data

    return gnome(mas)[m]


try:
    m = int(input('Введите натуральное число: '))
    MY_MASS = [uniform(0, 50) for i in range(m * 2 + 1)]
    MY_MASS_1 = MY_MASS[:]
    MY_MASS_2 = MY_MASS[:]
    print(MY_MASS)
    print(f'Медиана check: {median(MY_MASS)}')
    print(timeit(f'median({MY_MASS})', setup='from statistics import median', number=1))
    print(f'Медиана без сортировки: {without_sort(MY_MASS_1)}')
    print(timeit(f'without_sort({MY_MASS_1})', setup='from __main__ import without_sort', number=1))
    print(f'С гномьей сортировкой: {with_sort(MY_MASS_2)}')
    print(timeit(f'with_sort({MY_MASS_2})', setup='from __main__ import with_sort', number=1))
except ValueError:
    print('Число!!')
