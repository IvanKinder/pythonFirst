"""
Пробовал удалять нечетные элементы из имеющегося списка, но это не всегда было быстрее, а на больших списках медленнее
Так тоже медленнее, но выглядит красивее
Не смог придумать вариант быстрее, чем имеющийся
"""
import timeit
numbers = [n for n in range(1000)]

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    return [nums.index(n) for n in nums if n % 2 == 0]

print(f'Первая функция: {func_1(numbers)}')
print(f'Вторая функция: {func_2(numbers)}')
print(timeit.timeit(f'func_1({numbers})', setup='from __main__ import func_1', number=1))
print(timeit.timeit(f'func_2({numbers})', setup='from __main__ import func_2', number=1))