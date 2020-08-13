"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
from collections import defaultdict
from collections import deque

TRANS_DICT = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}


class NUM16:

    def __init__(self, letters):
        self.n16 = letters[::-1]
        self.trans_dict = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
        self.n2 = self.convert_to_2()

    def convert_to_2(self):
        converted = defaultdict(int)
        con_nam = 0
        for i in range(len(self.n16)):
            if self.n16[i].isdigit():
                converted[i] = int(self.n16[i])
            else:
                converted[i] = self.trans_dict[self.n16[i].lower()]
        for key, value in converted.items():
            con_nam += value * (16 ** key)
        return con_nam

    def __add__(self, other):
        a = self.n2 + other.n2
        return a

    def __mul__(self, other):
        pass


def convert_to_16(a):
    converted = deque()
    converted2 = deque()
    for key, value in TRANS_DICT.items():
        if a == value:
            return key
    if a < 10:
        return str(a)

    def recursion_convert(numb):
        if numb < 16:
            converted.appendleft(numb)
            return converted
        else:
            converted.appendleft(numb % 16)
            recursion_convert(numb // 16)

    if a > 15:
        recursion_convert(a)
    for nu2 in converted:
        if nu2 not in TRANS_DICT.values():
            converted2.append(str(nu2))
        else:
            for key, value in TRANS_DICT.items():
                if nu2 == value:
                    converted2.append(key)
    return converted2


n16_1 = NUM16([j for j in input('Введите первое шестнадцатиричное число: ')])
n16_2 = NUM16([j for j in input('Введите второе шестнадцатиричное число: ')])
print(n16_1.n2)
print(n16_2.n2)
print(n16_1.n2 + n16_2.n2)
print(f"{''.join(n16_1.n16[::-1])} + {''.join(n16_2.n16[::-1])} = {''.join(convert_to_16(n16_1 + n16_2)).upper()}")
