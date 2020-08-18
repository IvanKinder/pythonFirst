"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
from random import randint
from timeit import timeit
from memory_profiler import memory_usage

MY_MASS = [randint(-100, 100) for i in range(11)]


def puz_sort(mass):
    for j in range(len(mass) - 1):
        for i in range(len(mass) - 1):
            if mass[i] < mass[i + 1]:
                a = mass[i]
                mass[i] = mass[i + 1]
                mass[i + 1] = a
    return mass


# Поскольку вероятность получить уже отсортированный массив при случайной генерации мала, придумал другую оптимизацию
def puz_sort_optimized(mass):
    for j in range(len(mass) - 1):
        for i in range(len(mass) - 1):
            if mass[i] < mass[i + 1]:
                a = mass[i]
                mass[i] = mass[i + 1]
                mass[i + 1] = a
            else:
                break
    return mass


print(MY_MASS)

m1 = memory_usage()
print(puz_sort(MY_MASS))
m2 = memory_usage()
print(
    f"Время выполнения без доработок: {timeit(f'puz_sort({MY_MASS})', setup='from __main__ import puz_sort', number=1)}")
print(f'Потрачено памяти без доработок: {m2[0] - m1[0]} MiB')


m1 = memory_usage()
print(puz_sort_optimized(MY_MASS))
m2 = memory_usage()
print(
    f"Время выполнения с доработками: {timeit(f'puz_sort_optimized({MY_MASS})', setup='from __main__ import puz_sort_optimized', number=1)}")
print(f'Потрачено памяти с доработками: {m2[0] - m1[0]} MiB')
