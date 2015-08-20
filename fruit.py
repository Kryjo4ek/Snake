__author__ = 'vsevolod'
from sprite import *
# import random


class Fruit(Sprite):


    def __init__(self, pos):
        Sprite.__init__(self, pos, (0, 255, 0))
