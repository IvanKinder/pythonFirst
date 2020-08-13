from collections import deque
from timeit import timeit


def li1():
    return [i for i in range(1000)]


def de1():
    return deque(i for i in range(1000))


my_list = li1()
my_deque = de1()


def li_app():
    return my_list.append(1002)


def de_app():
    return my_deque.append(1002)


def li_ins():
    return my_list.insert(0, 1002)


def de_ins():
    return my_deque.appendleft(1002)


print(timeit('li1()', setup='from __main__ import li1', number=1))  # заполнить саисок быстрее
print(timeit('de1()', setup='from __main__ import de1', number=1))

print(timeit('li_app()', setup='from __main__ import li_app', number=1))  # добавить в конец списка быстрее
print(timeit('de_app()', setup='from __main__ import de_app', number=1))

print(timeit('li_ins()', setup='from __main__ import li_ins', number=1))
print(timeit('de_ins()', setup='from __main__ import de_ins', number=1))  # добавить в начало у дека быстрее

'''Всё, как и рассказали на лекции'''
