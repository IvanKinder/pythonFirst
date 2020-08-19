"""
Долго придумывал собственную реализацию сортировки слиянием, но за неимением времени скопипастил из интернета,
однако при сравнении, пузырек оказался в разы быстрее...странно
"""
from random import uniform
from timeit import timeit

MY_MASS = [uniform(0, 50) for i in range(int(input('Введите количество элементов: ')))]
J_TXT = 'Время сортировки '


def merge_sort(mass):
    if len(mass) > 1:
        mid = len(mass) // 2
        left = mass[:mid]
        right = mass[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                mass[k] = left[i]
                i = i + 1
            else:
                mass[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            mass[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            mass[k] = right[j]
            j = j + 1
            k = k + 1
    return mass


def sort_very_good(mass):
    flag = False
    for j in range(len(mass) - 1):
        for i in range(len(mass) - 1):
            if mass[i] > mass[i + 1]:
                a = mass[i]
                mass[i] = mass[i + 1]
                mass[i + 1] = a
            else:
                flag = True
        if flag:
            break
    return mass


print(f'Исходный массив: {MY_MASS}')
print(f'Сортировка слиянием: {merge_sort(MY_MASS)}')
print(f'Сортировка пузырьком: {sort_very_good(MY_MASS)}')
print(
    f"{J_TXT}слиянием: {timeit(f'merge_sort({MY_MASS})', setup='from __main__ import merge_sort', number=1)}")
print(
    f"{J_TXT}пузырьком: {timeit(f'sort_very_good({MY_MASS})', setup='from __main__ import sort_very_good', number=1)}")
