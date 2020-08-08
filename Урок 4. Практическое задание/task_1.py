"""
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
Добавьте аналитику: что вы сделали и почему
"""
import timeit
numbers = [12, 13, 11, 111, 43, 24, 22222, 2, 22, 77]

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

print(f'Первая функция: {func_1(numbers)}')
print(f'Вторая функция: {func_2(numbers)}')
print(timeit.timeit(f'func_1({numbers})', setup='from __main__ import func_1', number=10000))
print(timeit.timeit(f'func_2({numbers})', setup='from __main__ import func_2', number=10000))