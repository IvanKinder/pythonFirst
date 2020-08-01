SUM = 0


def progression(n, s):
    if n == 1:
        return s + 1
    else:
        s += (-0.5) ** (n - 1)
        return progression(n - 1, s)


try:
    print(progression(int(input('Введите количество чисел ряда: ')), SUM))
except ValueError:
    print('Введите натуральное число!!!\n')
except RecursionError:
    print('Вы ввели нулевое количетсво элементов!\n')