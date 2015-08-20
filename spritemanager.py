__author__ = 'vsevolod'
import pygame



class SpriteManager(object):
    __instance = None

    @staticmethod
    def inst():
        if SpriteManager.__instance == None:
            SpriteManager.__instance = SpriteManager()
        return SpriteManager.__instance

    def __init__(self):
        if SpriteManager.__instance != None:
            raise PermissionError

        self.screen = pygame.display.set_mode((1024, 768))
        self.setSprite = set()

    def update(self):
        self.screen.fill((0, 0, 0))
        for spriteOne in self.setSprite:
            spriteOne.render(self.screen)
        pygame.display.update()

    def addSprite(self, sprite):
        self.setSprite.add(sprite)
