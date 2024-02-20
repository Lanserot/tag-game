import sys
from Storage import Storage


class LogicControl:
    def __init__(self, storage: Storage):
        self.storage = storage

    def checkCantChangePosition(self, row: int, coll: int):
        if (0 <= row < len(self.storage.getFieldClass().field)) and (0 <= coll < len(self.storage.getFieldClass().field[0])):
            self.storage.getMemoryClass().countStep += 1
            return False
        return True

    def changePosition(self, row: int, coll: int, changeRow: int, changeColl: int):
        if self.checkCantChangePosition(changeRow, changeColl):
            return

        self.updateFieldPosition(row, coll, changeRow, changeColl)

    def updateFieldPosition(self, row: int, coll: int, changeRow: int, changeColl: int):
        self.storage.getFieldClass().field[row][coll] = self.storage.getFieldClass().field[changeRow][changeColl]
        self.storage.getFieldClass().field[changeRow][changeColl] = self.storage.getFieldClass().PLAYER_NUM
        self.storage.getFieldClass().activePosition = [changeRow, changeColl]

    def handleKey(self, pygame):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.activeScreen()
                elif self.storage.getMemoryClass().activeRender == self.storage.getMenuClass().renderName:
                    self.activeMenu(event, pygame)
                elif self.storage.getMemoryClass().activeRender == self.storage.getFieldClass().renderName:
                    self.activeField(event, pygame)

    def activeMenu(self, event, pygame):
        if event.key == pygame.K_UP:
            self.storage.getMenuClass().btnUp()
        elif event.key == pygame.K_DOWN:
            self.storage.getMenuClass().btnDown()
        elif event.key == pygame.K_RETURN:
            self.storage.getMenuClass().btnEnter(self.storage, pygame)

    def activeField(self, event, pygame):
        row = self.storage.getFieldClass().activePosition[0]
        coll = self.storage.getFieldClass().activePosition[1]

        if event.key == pygame.K_UP:
            self.changePosition(row, coll, row - 1, coll)
        elif event.key == pygame.K_DOWN:
            self.changePosition(row, coll, row + 1, coll)
        elif event.key == pygame.K_LEFT:
            self.changePosition(row, coll, row, coll - 1)
        elif event.key == pygame.K_RIGHT:
            self.changePosition(row, coll, row, coll + 1)

    def activeScreen(self):
        if self.storage.getMemoryClass().activeRender == self.storage.getFieldClass().renderName:
            self.storage.getMemoryClass().activeRender = self.storage.getMenuClass().renderName
            self.storage.getMenuClass().activeBtnNum = 0
            self.storage.getMenuClass().resetBtnActive()
        else:
            self.storage.getMemoryClass().activeRender = self.storage.getFieldClass().renderName
