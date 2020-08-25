"""Работа над улучшенным вариантом продолжается..."""
from collections import Counter, deque, defaultdict

MY_STRING = "beep boop beer!"
from task_2 import BinaryTree

dicci = {}
for let in MY_STRING:
    dicci[let] = MY_STRING.count(let)
    spissi = sorted(dicci.items(), key=lambda x: x[1])

spissi2 = spissi[:]

for i in range(1):
    new_fetch = BinaryTree(spissi2.pop(i) + spissi2.pop(i))
# a = spissi2.index('p', new_fetch.get_root_val()[1] + new_fetch.get_root_val()[3])
# print(a)
# spissi2.insert(a, new_fetch.get_root_val())
# for i in range(len(spissi2)):
#     if spissi2[i][1] <= new_fetch.get_root_val() <= spissi2[i + 1][1]:
#         spissi2.insert(i, new_fetch)
#         break


print(MY_STRING)
print(dicci)
print(spissi)
print(new_fetch.get_root_val())
print(spissi2)
