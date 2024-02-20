import random
from Storage import Storage


class Field:
    renderName = 'field'

    lvl = 'lvl1'

    BLOCK_SIZE = 50

    PLAYER_NUM = 0

    activePosition = [0, 0]

    field = []

    def generate_field(self):
        size = 3
        if self.lvl == 'lvl2':
            size = 4
        elif self.lvl == 'lvl3':
            size = 5

        self.field = []
        count = 1
        for i in range(size):
            row = []
            for j in range(size):
                row.append(count)
                count += 1
            self.field.append(row)
        self.field[size - 1][size - 1] = 0
        self.correctField = self.field.copy()

    def initLvl(self):
        self.generate_field()
        self.shuffleField()

    def findActivePosition(self):
        for i, row in enumerate(self.field):
            for j, element in enumerate(row):
                if element == 0:
                    self.activePosition[0] = i
                    self.activePosition[1] = j

    def shuffleField(self):
        random.shuffle(self.field)
        self.findActivePosition()

    def __init__(self):
        self.correctField = None
        self.initLvl()

