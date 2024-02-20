from Storage import Storage


class Renderer:
    WHITE_COLOR = (255, 255, 255)
    LITE_GREY_COLOR = (200, 200, 200)
    GREY_COLOR = (150, 150, 150)
    BLACK_COLOR = (0, 0, 0)

    def render(self):
        if self.storage.getMemoryClass().activeRender == self.storage.getFieldClass().renderName:
            self.renderFieldscreen()
        elif self.storage.getMemoryClass().activeRender == self.storage.getMenuClass().renderName:
            self.renderMenuScreen()

    def renderMenuScreen(self):
        self.pygame.draw.rect(self.screen, self.WHITE_COLOR, (0, 0, 640, 480))

        for button in self.storage.getMenuClass().buttons:
            font = self.pygame.font.Font(None, 36)
            text = button.text
            if button.active:
                self.pygame.draw.rect(self.screen, self.LITE_GREY_COLOR, (25, 75 + button.id * 50, 100, 50))

            self.drawText(text, font, 50, 100 + button.id * 50)

    def renderFieldscreen(self):
        self.pygame.draw.rect(self.screen, self.WHITE_COLOR, (0, 0, 640, 480))
        font = self.pygame.font.Font(None, 36)
        text = 'Количество шагов : ' + str(self.storage.getMemoryClass().countStep)
        self.drawText(text, font,
                      len(self.storage.getFieldClass().field[0]) * self.storage.getFieldClass().BLOCK_SIZE + 150, 20)
        self.drawField(font)

    def drawField(self, font):
        for line_index, line in enumerate(self.storage.getFieldClass().field):
            for block_index, block in enumerate(line):
                self.pygame.draw.rect(self.screen, self.LITE_GREY_COLOR,
                                      (self.storage.getFieldClass().BLOCK_SIZE * block_index,
                                       self.storage.getFieldClass().BLOCK_SIZE * line_index,
                                       self.storage.getFieldClass().BLOCK_SIZE,
                                       self.storage.getFieldClass().BLOCK_SIZE))
                self.pygame.draw.rect(self.screen, self.GREY_COLOR,
                                      (self.storage.getFieldClass().BLOCK_SIZE * block_index + 5,
                                       self.storage.getFieldClass().BLOCK_SIZE * line_index + 5,
                                       self.storage.getFieldClass().BLOCK_SIZE - 10,
                                       self.storage.getFieldClass().BLOCK_SIZE - 10))

                if block == 0:
                    continue

                self.drawText(str(block), font, self.storage.getFieldClass().BLOCK_SIZE * block_index + 20,
                              self.storage.getFieldClass().BLOCK_SIZE * line_index + 20)

    def __init__(self, storage: Storage, pygame, screen):
        self.storage = storage
        self.pygame = pygame
        self.screen = screen

    def drawText(self, text: str, font, x: int, y: int):
        text = font.render(text, True, self.BLACK_COLOR)
        text_rect = text.get_rect()
        text_rect.centerx = x
        text_rect.centery = y
        self.screen.blit(text, text_rect)
