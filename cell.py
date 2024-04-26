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
        self.selected = False
    
    def set_cell_value(self,value):
        self.value = value

    def set_sketched_value(self,value):
        self.sketch = value

    def c_select(self):
        self.selected = True
        print(f"Cell at ({self.row+1}, {self.col+1}) selected.")  # DEBUG

    def deselect(self):
        self.selected = False
        print(f"Cell at ({self.row+1}, {self.col+1}) deselected.")  # DEBUG


    # Finished?
    def draw(self):
        cell_size = 100
        x = self.col * cell_size
        y = self.row * cell_size
        # print(x, y) # DEBUG
        # print(self.value) # DEBUG
        pygame.draw.rect(self.screen, White, (x, y, cell_size, cell_size))
        pygame.draw.rect(self.screen, Red if self.selected else Black, (x, y, cell_size, cell_size), 1)

        if self.value != 0:
            font = pygame.font.Font(None, 36)
            text = font.render(str(self.value), True, Black)
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            self.screen.blit(text, text_rect)

        if self.sketch != 0:
            font = pygame.font.Font(None, 40)
            text = font.render(str(self.sketch), True, (200,200,200))
            text_rect = text.get_rect(center=(x + 11, y + 15))
            self.screen.blit(text, text_rect)


