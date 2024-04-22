import pygame, sys
from board import *

def draw_game_start(screen):
    pass
def draw_game_over():
    pass
def game_start():
    pass


if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((900, 1000))
    screen.fill((255,255,255))
    new_board = Board(900, 900, screen, "easy")
    pygame.display.set_caption("Sudoku")

    new_board.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()