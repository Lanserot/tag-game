from Field import Field
from LogicControl import LogicControl
import pygame
from Memory import Memory
from Storage import Storage
from Menu import Menu
from Renderer import Renderer


class Main:

    def start(self):
        while True:
            self.storage.getLogicClass().handleKey(self.pygame)
            self.storage.getRendererClass().render()
            pygame.display.flip()

    def __init__(self):
        pygame.init()
        self.pygame = pygame
        self.screen = pygame.display.set_mode((640, 480))

        self.storage = Storage()
        self.storage.fieldClass = Field()
        self.storage.memoryClass = Memory()
        self.storage.menuClass = Menu()
        self.storage.rendererClass = Renderer(self.storage, self.pygame, self.screen)
        self.storage.logicClass = LogicControl(self.storage)


mainClass = Main()
mainClass.start()
