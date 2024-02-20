from Button import Button
from Storage import Storage
import sys


class Menu:
    renderName = 'menu'

    activeBtnNum = 0

    buttons = [
        Button(1, "3x3", "lvl1", True),
        Button(2, "4x4", "lvl2"),
        Button(3, "5x5", "lvl3"),
        Button(4, "Выход", "exit"),
    ]

    def btnEnter(self, storage: Storage, pygame):
        tag = self.buttons[self.activeBtnNum].tag
        if tag == "exit":
            pygame.quit()
            sys.exit()

        if tag != storage.getFieldClass().lvl:
            storage.getFieldClass().lvl = tag
            storage.getFieldClass().initLvl()
            storage.getMemoryClass().countStep = 0
            storage.getMemoryClass().activeRender = storage.getFieldClass().renderName

    def btnUp(self):
        if self.activeBtnNum == 0:
            self.activeBtnNum = len(self.buttons) - 1
        else:
            self.activeBtnNum -= 1

        self.resetBtnActive()

    def btnDown(self):
        if len(self.buttons) - 1 == self.activeBtnNum:
            self.activeBtnNum = 0
        else:
            self.activeBtnNum += 1
        self.resetBtnActive()

    def resetBtnActive(self):
        for button in self.buttons:
            button.active = False
        self.buttons[self.activeBtnNum].active = True
