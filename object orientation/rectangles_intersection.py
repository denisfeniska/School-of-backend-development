class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def intersection(self, rect):
        if ((rect.x >= self.x + self.w) or (rect.y >= self.y + self.h) or (self.x == rect.x + rect.w) or (self.y == rect.y + rect.h)):
            return None
        else:
            result_rect = Rectangle(0, 0, 0, 0)
            result_rect.x = max(self.x, rect.x)
            result_rect.y = max(self.y, rect.y)
            result_rect.w = min(self.x + self.w, rect.x + rect.w) - result_rect.x
            result_rect.h = min(self.y + self.h, rect.y + rect.h) - result_rect.y
            return result_rect

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h



rect1 = Rectangle(3, 5, 2, 1)
rect2 = Rectangle(1, 2, 10, 10)
rect3 = rect1.intersection(rect2)
if rect3 is None:
 print('No intersection')
else:
 print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())