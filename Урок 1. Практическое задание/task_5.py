class StackClass:
    def __init__(self, max_n):
        self.elements = [[]]
        self.max_n = max_n

    def is_empty(self):  # пустой ли стек
        return self.elements == [[]]

    def push_in(self, el):  # добавить элемент
        if len(self.elements[-1]) < self.max_n:
            self.elements[-1].append(el)
        else:
            self.elements.append([el])

    def pop_out(self):  # убрать последний элемент элемент
        return self.elements[-1].pop()

    def get_val(self):  # вернуть последний элемент
        return self.elements[-1][len(self.elements[-1]) - 1]

    def stack_size(self):  # общее количество тарелок
        return (len(self.elements) - 1) * len(self.elements[0]) + len(self.elements[-1])

    def drop_last_stack(self):  # убрать последнюю стопку тарелок
        return self.elements.pop()

    def drop_full_stack(self):  # убрать все тарелки
        self.elements = [[]]


NUM = int(input('Введите пороговое значение для стопки тарелок: '))
STACK_OBJ = StackClass(NUM)

for i in range(10):
    STACK_OBJ.push_in(1)

print(STACK_OBJ.elements, '\n', STACK_OBJ.get_val(),
      '\n', STACK_OBJ.stack_size(), '\n', STACK_OBJ.is_empty())
STACK_OBJ.drop_full_stack()
print(STACK_OBJ.elements)
