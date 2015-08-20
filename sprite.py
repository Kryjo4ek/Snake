__author__ = 'vsevolod'

from pygame import *
from spritemanager import *
from vector import *
from grid import *
# import random


class Sprite:

    def __init__(self, pos, color):
        self.size = Vector(100, 100)
        self.gridPos = pos
        self.pos = pos.multiply(100)
        self.oneSprite = Surface((self.size.x, self.size.y))
        self.oneSprite.fill(color)

        SpriteManager.inst().addSprite(self)
        Grid.inst().addSpriteGrid(self)

    def move(self, pos):
        Grid.inst().deleteSriteGrid(self.gridPos)
        self.gridPos = pos
        Grid.inst().addSpriteGrid(self)

    def render(self, screen):

        screen.blit(self.oneSprite, (self.pos.x, self.pos.y))


