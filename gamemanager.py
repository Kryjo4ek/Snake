__author__ = 'vsevolod'
# import sys
from pygame import *

from spritemanager import *
# from sprite import *
from fruit import *
from vector import *


class GameManager:


    def start(self):

        Sprite(Vector(1, 0), (255, 255, 255))
        Sprite(Vector(0, 0), (255, 255, 255))
        Sprite(Vector(1, 1), (255, 255, 255))
        Fruit(Vector(1, 2))


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            SpriteManager.inst().update()