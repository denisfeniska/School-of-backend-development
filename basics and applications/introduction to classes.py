class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        self.v = v
        if self.count + self.v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        self.v = v
        if self.can_add(self.v):
            self.count += self.v
        
