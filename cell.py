Black = (0,0,0)
White = (255,255,255)
import pygame

class Cell:
    def __init__(self,value,row,col,screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch = 0
    
    def set_cell_value(self,value):
        self.value = value

    def set_sketched_value(self,value):
        self.sketch = value

    def draw(self): # Feel as though I'm missing some details but the main idea is there.
        x = self.col
        y = self.row

        pygame.draw.rect(self.screen, White, (x, y, self),1)

        if self.value != 0:
            font = pygame.font.Font(None, 36)
            text = font.render(str(self.value), True, Black)
            text_rect = text.get_rect(center=(x,y))
            self.screen.blit(text, text_rect)

