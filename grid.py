__author__ = 'vsevolod'
from cell import *
import random
# from vector import *
from fruit import *


class Grid:

    __instance = None

    @staticmethod
    def inst():
        if Grid.__instance == None:
            Grid.__instance = Grid()
        return Grid.__instance

    def __init__(self):
        if Grid.__instance != None:
            raise PermissionError

        self.SIZE = 10
        self.cells = [[None] * self.SIZE for i in range(self.SIZE)]


        for i in range(0, self.SIZE):
            for j in range(0, self.SIZE):
                self.cells[i][j] = Cell(i, j)

        self.fruit = Fruit(Vector(10, 10))

    def getCell(self, pos):
        return self.cells[pos.x][pos.y]

    def addSpriteGrid(self, sprite):
        self.cells[sprite.gridPos.x][sprite.gridPos.y] = sprite

    def deleteSpriteGrid(self, pos):
        self.cells[pos.x][pos.y] = None

    def randomMovePos(self):
        self.fruit.move(Vector(random.randint(0, self.SIZE), random.randint(0, self.SIZE)))

