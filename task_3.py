STACK = []


def reverse(digit):
    if digit // 10 == 0:
        STACK.insert(0, digit)
        for i in STACK:
            print(i, end='')
    else:
        STACK.insert(0, digit // 10 ** (len(str(digit)) - 1))
        return reverse(digit % 10 ** (len(str(digit)) - 1))


try:
    reverse(int(input('Введите целое число: ')))
except ValueError:
    print('Вводите целые числа!!')
