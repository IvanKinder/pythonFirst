import cProfile
import timeit

NUMBER = 123456789876543212345678987654321234567898765432198765432198765432165657474838392920101


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
cProfile.run(f'revers_1({NUMBER})')  # функция вызвалась 88 раз
cProfile.run(f'revers_2({NUMBER})')  # ничего особенного cProfile не показал
cProfile.run(f'revers_3({NUMBER})')  # ничего особенного cProfile не показал
print(timeit.timeit(f'revers_1({NUMBER})', setup='from __main__ import revers_1', number=1))
# не понял, почему рекурсия быстрее, чем цикл в данной задаче
print(timeit.timeit(f'revers_2({NUMBER})', setup='from __main__ import revers_2', number=2))
# последняя эффективнее всех, потому что ничего не считатала
print(timeit.timeit(f'revers_3({NUMBER})', setup='from __main__ import revers_3', number=3))
