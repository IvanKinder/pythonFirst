class QueueClass:
    def __init__(self):
        self.elements = []
        self.done_tasks = []

    def is_empty(self):  # пустая ли очередь
        return self.elements == []

    def to_queue(self, item):  # добавить в очередь
        self.elements.insert(0, item)

    def from_queue(self):  # убрать из очереди
        return self.elements.pop()

    def size(self):  # размер очереди
        return len(self.elements)

    def done_task(self):  # добавить задачу в список выполненных
        self.done_tasks.append(self.from_queue())

    def to_rework(self, qu_obj):  # добавить задачу в очередь для корректировки
        qu_obj.to_queue(self.from_queue())


BASE_TASKS = QueueClass()
for i in range(10):  # наполняем очередь задачами
    BASE_TASKS.to_queue('task_' + str(i))
print('Всего задач: ', BASE_TASKS.elements)

for i in range(4):  # решаем несколько задач
    BASE_TASKS.done_task()
print('Осталось задач: ', BASE_TASKS.elements)
print('Сделанные задачи: ', BASE_TASKS.done_tasks)

REWORK_TASKS = QueueClass()  # создаем очередь для корректировочных задач

BASE_TASKS.to_rework(REWORK_TASKS)  # отправляем пару заданий в очередь для корректировки
BASE_TASKS.to_rework(REWORK_TASKS)

print('Осталось задач: ', BASE_TASKS.elements)
print('Задачи для доработки: ', REWORK_TASKS.elements)
