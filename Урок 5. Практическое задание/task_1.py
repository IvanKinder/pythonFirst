from collections import deque


COMPANIES = deque()

for i in range(int(input('Введите количество предприятий для расчета прибыли: '))):
    COMPANY = {}
    comp_name = input(f'Введите название {i + 1} предприятия: ')
    COMPANY[comp_name] = [float(input(f'Введите прибыль за {m + 1} квартал: ')) for m in range(4)]
    COMPANIES.append(COMPANY)

AVG_MONEY = sum([sum(max(i.values())) / len(COMPANIES) for i in COMPANIES])

print(f'Средняя годовая прибыль всех предприятий: {AVG_MONEY}')

MORE_COMPS = set()
LESS_COMPS = set()

for comp in COMPANIES:
    for key in comp.keys():
        if sum(max(comp.values())) > AVG_MONEY:
            MORE_COMPS.add(key)
        elif sum(max(comp.values())) < AVG_MONEY:
            LESS_COMPS.add(key)

print(f'Предприятия с прибылью выше среднего: {MORE_COMPS}')
print(f'Предприятия с прибылью ниже среднего: {LESS_COMPS}')
