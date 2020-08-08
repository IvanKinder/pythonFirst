import timeit

NUMBERS = [n for n in range(100000)]
SETUP1 = 'from __main__ import func_1'
SETUP2 = 'from __main__ import func_2'


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):  # заменил стандартный итератор на сахарок питона
    new_arr = []
    for n in nums:
        if n % 2 == 0:
            new_arr.append(n)
    return new_arr


print(f'Первая функция: {func_1(NUMBERS)}')
print(f'Вторая функция: {func_2(NUMBERS)}')
print(f"Среднее время первой функции: {timeit.timeit(f'func_1({NUMBERS})', setup=SETUP1, number=100) / 100}")
print(f"Среднее время второй функции: {timeit.timeit(f'func_2({NUMBERS})', setup=SETUP2, number=100) / 100}")
