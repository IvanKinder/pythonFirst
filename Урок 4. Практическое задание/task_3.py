"""
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
NUMBER = 123456789
def revers(enter_num, revers_num=0):  # функция ничего не возвращает, исправил ниже
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return int(revers_num)  # добавил здесь то, что возвращать
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)  # добавил здесь return


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)  # добавил int чтоб было везде одинаково


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

print(revers(NUMBER))  # видно, что функция ничего не возвращает
print(revers_1(NUMBER))
print(revers_2(NUMBER))
print(revers_3(NUMBER))