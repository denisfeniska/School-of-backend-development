class Summator():
    def __init__(self) -> None:
        self.summa = 0

    def transform(self, n):
        return n

    def suma(self, N):
        for i in range(1, N + 1):
            summa += self.transform(i)
        return summa

class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2

class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3

class PowerSummator(Summator):
    def __init__(self, b) -> None:
        self.b = b

    def transform(self, n):
        return n ** self.b
