"""
Сырой вариант по коду из лекции
"""
from collections import Counter, deque, defaultdict

MY_STRING = "beep boop beer!"


def binary_haf(count_list):
    freq_dict = Counter(count_list)
    freq_list = deque(sorted(freq_dict.items(), key=lambda item: item[1]))
    if len(freq_list) != 1:
        while len(freq_list) > 1:
            freq = freq_list[0][1] + freq_list[1][1]
            knot = {0: freq_list.popleft()[0],
                    1: freq_list.popleft()[0]}

            for i, new_freq in enumerate(freq_list):
                if freq > new_freq[1]:
                    continue
                else:
                    freq_list.insert(i, (knot, freq))
                    break
            else:
                freq_list.append((knot, freq))
    else:
        freq = freq_list[0][1]
        knot = {0: freq_list.popleft()[0]}
        freq_list.append((knot, freq))
    return freq_list[0][0]


code_table = {}


def code_haf(tree, path=''):
    if type(tree) != dict:
        code_table[tree] = path
    else:
        code_haf(tree[0], path=f'{path}0')
        code_haf(tree[1], path=f'{path}1')


code_haf(binary_haf(MY_STRING))

for i in MY_STRING:
    print(code_table[i], end=' ')
print()
