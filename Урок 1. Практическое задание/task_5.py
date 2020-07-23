class StackClass:
    def __init__(self, n):
        self.elements = [[]]
        self.n = n

    def is_empty(self):
        return self.elements == [[]]

    def push_in(self, el):
        if len(self.elements[-1]) < self.n:
            self.elements[-1].append(el)
        else:
            self.elements.append([el])

    def pop_out(self):
        return self.elements[-1].pop()

    def get_val(self):
        return self.elements[-1][len(self.elements[-1]) - 1]

    def stack_size(self):
        return (len(self.elements) - 1) * len(self.elements[0]) + len(self.elements[-1])

    def drop_last_stack(self):
        return self.elements.pop()

    def drop_full_stack(self):
        self.elements = [[]]


n = int(input('Введите пороговое значение для стопки тарелок: '))
STACK_OBJ = StackClass(n)

for i in range(10):
    STACK_OBJ.push_in(1)

print(STACK_OBJ.elements, '\n', STACK_OBJ.get_val(), '\n', STACK_OBJ.stack_size(), '\n', STACK_OBJ.is_empty())
STACK_OBJ.drop_full_stack()
print(STACK_OBJ.elements)