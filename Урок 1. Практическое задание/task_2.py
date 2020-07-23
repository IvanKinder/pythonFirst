import random


def min_digit_n2(list_ob):
    min_dig = list_ob[0]
    i = 0
    while i < len(list_ob):
        for digit in list_ob:
            if list_ob[i] < digit and list_ob[i] < min_dig:
                min_dig = list_ob[i]
        i += 1

    return print(min_dig)


def min_digit_n(list_ob):
    min_dig = list_ob[0]
    for digit in list_ob:
        if digit < min_dig:
            min_dig = digit
    return print(min_dig)


MY_LIST = [random.randint(0, 100) for i in range(10)]
print(MY_LIST)

min_digit_n2(MY_LIST)
min_digit_n(MY_LIST)
