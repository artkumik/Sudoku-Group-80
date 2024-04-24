Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
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


    # Not Finished
    def draw(self): # Feel as though I'm missing some details but the main idea is there.
        cell_size = 99  # When set to 100, the board is not filled, 99 'works' but is scuffed.
        # I feel as though it has to do with the range called within the Board class.
        x = self.col * cell_size
        y = self.row * cell_size
        # print(x, y) # DEBUG

        pygame.draw.rect(self.screen, Red, (x, y, cell_size, cell_size), 1)

        if self.value != 0:
            # print(self.value) # DEBUG
            font = pygame.font.Font(None, 36)
            text = font.render(str(self.value), True, Black)
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            self.screen.blit(text, text_rect)

