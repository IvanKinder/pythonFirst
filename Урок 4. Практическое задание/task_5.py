"""
НЕ СПРАВИЛСЯ!

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).
Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)
Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


simple_digits = {1: 2, 2: 3}


def eratosfen(i):
    j = 2
    k = 5
    for n in range(3, i + 1):
        simple_digits[n] = 0
    for itr in range(1, len(simple_digits.keys())):
        if k % simple_digits[itr] == 0:
            k += 2
            continue
        else:
            simple_digits[j + 1] = k
            j += 1
    return simple_digits


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(eratosfen(i))
