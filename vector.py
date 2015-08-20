__author__ = 'vsevolod'


class Vector():

    def __init__(self, x, y):
        self.x, self.y = x, y

    def multiply(self, factor):
        self.x *= factor
        self.y *= factor
        return self