COMPANIES = {'A': 3000000000, 'B': 6500000000,
             'C': 2300000000, 'D': 3250000000,
             'E': 9000000000, 'F': 2000000500}


# O(n) - эффективнее, потому что намного короче, использует встроенные функции языка
# и все-таки сложность такого же порядка, но меньше, чем у второго алгоритма

def searching_1(my_dic):
    for key, value in my_dic.items():
        if value in sorted(my_dic.values())[-3:]:
            print(key)


# O(n)

def searching_2(my_dic):
    max_cost_1 = 0
    max_cost_2 = 0
    max_cost_3 = 0
    for value in my_dic.values():
        if value > max_cost_3:
            max_cost_3 = value
    for value in my_dic.values():
        if max_cost_3 > value > max_cost_2:
            max_cost_2 = value
    for value in my_dic.values():
        if max_cost_2 > value > max_cost_1:
            max_cost_1 = value
    for key in my_dic.keys():
        if my_dic[key] in [max_cost_1, max_cost_2, max_cost_3]:
            print(key)


searching_1(COMPANIES)
print('--------------------------')
searching_2(COMPANIES)
