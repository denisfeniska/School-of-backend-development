import copy
from PIL import Image as im
from PIL import ImageDraw as draw


class Drawer:
    def __init__(self, draw_map, cell_size, color='black') -> None:
        self.draw_map = draw_map
        self.cell_size = cell_size
        self.number_color = {number: color for number in self.numbers()}

    def numbers(self):
        new_L = copy.deepcopy(self.draw_map)
        return list(sorted(list(set(new_L))))

    def set_color(self, number, color):
        self.number_color[number] = color

    def set_cell_size(self, cell_size):
        self.cell_size = cell_size

    def size(self, flag=True):
        if flag:
            return len(self.draw_map[0]) * self.cell_size, len(self.draw_map) * self.cell_size
        return len(self.draw_map[0]), len(self.draw_map)

    def draw(self):
        image = im.new("RGB", (self.size()[0], self.size()[1]), (0, 0, 0))
        desk = draw.Draw(image)
        size = self.size(flag=False)

        for i in range(size[1]):
            for j in range(size[0]):
                desk.rectangle((self.cell_size * j, self.cell_size * i,
                                self.cell_size * (j + 1) - 1, self.cell_size * (i + 1) - 1),
                               fill=self.number_color[self.draw_map[i][j]])

        return image


