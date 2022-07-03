class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.buffer = []

    def add(self, *a):
        # добавить следующую часть последовательности
        self.a = a
        self.buffer += self.a
        while True:
            if len(self.buffer) >= 5:
                print(sum(self.buffer[0:5]))
                self.buffer = self.buffer[5:]
            else:
                break

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.buffer

