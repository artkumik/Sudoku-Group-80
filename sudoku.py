import copy
import pygame, sys
from board import *
from sudoku_generator import SudokuGenerator

FontColor = (255, 50, 255)
Black = (0,0,0)
White = (255,255,255)
total_width = 900
total_height = 1000


def draw_game_start(screen):
    #FINISHED
    # font sizes
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    screen.fill(White)

    # creating title
    title_surface = start_title_font.render("Welcome to Sudoku", 0, FontColor)
    select_surface = start_title_font.render("Select Game Mode:", 0, FontColor)
    title_rectangle = title_surface.get_rect(center=(total_width // 2, total_height // 2 - 250))
    select_rectangle = title_surface.get_rect(center=(total_width // 2, total_height // 2))
    screen.blit(title_surface, title_rectangle)
    screen.blit(select_surface, select_rectangle)

    # creating buttons
    easy_text = button_font.render("EASY", 0, White)
    med_text = button_font.render("MEDIUM", 0, White)
    hard_text = button_font.render("HARD", 0, White)

    # creates buttons and makes filled boxes with edges of boxes being 20 pixels away from text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(FontColor)
    easy_surface.blit(easy_text, (10, 10))
    med_surface = pygame.Surface((med_text.get_size()[0] + 20, med_text.get_size()[1] + 20))
    med_surface.fill(FontColor)
    med_surface.blit(med_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(FontColor)
    hard_surface.blit(hard_text, (10, 10))

    # button rectangles
    easy_rectangle = easy_surface.get_rect(center=(total_width // 2 - 255, total_height // 2 + 200))
    med_rectangle = med_surface.get_rect(center=(total_width // 2, total_height // 2 + 200))
    hard_rectangle = hard_surface.get_rect(center=(total_width // 2 + 265, total_height // 2 + 200))

    # draw button rectangles
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(med_surface, med_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    # returns string of "easy", "medium", "hard" or quits based on what is pressed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return "easy"
                elif med_rectangle.collidepoint(event.pos):
                    return "medium"
                elif hard_rectangle.collidepoint(event.pos):
                    return "hard"
        pygame.display.update()
def draw_game_over():
    #FINISHED
    text_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)
    screen.fill(White)

    # game over text and display
    text_surface = text_font.render("Game Over!", 0, FontColor)
    text_rectangle = text_surface.get_rect(center=(total_width // 2, total_height // 2 - 250))
    screen.blit(text_surface, text_rectangle)

    # restart button text
    res_text = button_font.render("RESTART", 0, White)

    # creates exit button fill with text
    res_surface = pygame.Surface((res_text.get_size()[0] + 20, res_text.get_size()[1] + 20))
    res_surface.fill(FontColor)
    res_surface.blit(res_text, (10, 10))

    # exit rectangle
    res_rectangle = text_surface.get_rect(center=(total_width // 2 + 80, total_height // 2))

    # draw full button rectangle
    screen.blit(res_surface, res_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if res_rectangle.collidepoint(event.pos):
                    return
        pygame.display.update()
    pass
def draw_game_win():
    #FINISHED
    text_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)
    screen.fill(White)

    # game over text and display
    text_surface = text_font.render("GAME WON!", 0, FontColor)
    text_rectangle = text_surface.get_rect(center=(total_width // 2, total_height // 2 - 250))
    screen.blit(text_surface, text_rectangle)

    # exit button text
    exit_text = button_font.render("EXIT", 0, White)

    # creates exit button fill with text
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(FontColor)
    exit_surface.blit(exit_text, (10, 10))

    # exit rectangle
    exit_rectangle = text_surface.get_rect(center=(total_width // 2 + 130, total_height // 2))

    # draw full button rectangle
    screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
    pass
def game_start(difficulty):
    # creates new board, titles, and buttons
    screen.fill(White)
    new_board = Board(900, 900, screen, difficulty)
    new_board.initialize_cells(altered_generated_Board) # <-- Called initialized method.
    new_board.draw()

    # font size
    button_font = pygame.font.Font(None, 60)

    # creating buttons
    reset_text = button_font.render("RESET", 0, White)
    restart_text = button_font.render("RESTART", 0, White)
    exits_text = button_font.render("EXIT", 0, White)

    # creates buttons and makes filled boxes with edges of boxes being 20 pixels away from text
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(FontColor)
    reset_surface.blit(reset_text, (10, 10))

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(FontColor)
    restart_surface.blit(restart_text, (10, 10))

    exits_surface = pygame.Surface((exits_text.get_size()[0] + 20, exits_text.get_size()[1] + 20))
    exits_surface.fill(FontColor)
    exits_surface.blit(exits_text, (10, 10))

    # button rectangles
    reset_rectangle = reset_surface.get_rect(center=(total_width // 2, total_height // 2 + 450))
    restart_rectangle = restart_surface.get_rect(center=(total_width // 2 + 220, total_height // 2 + 450))
    exits_rectangle = exits_surface.get_rect(center=(total_width // 2 - 180, total_height // 2 + 450))

    # draw button rectangles
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exits_surface, exits_rectangle)

    ############################################
    # ACTIONS FOR GAME MIGHT GO HERE VVVVVVVVV #
    ############################################
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exits_rectangle.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif reset_rectangle.collidepoint(event.pos):
                    return "reset"
                elif restart_rectangle.collidepoint(event.pos):
                    return "restart"
                    pass
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900, 1000))
    pygame.display.set_caption("Sudoku")

    # starts menu and gets difficulty
    str_difficulty = draw_game_start(screen)

    # Difficulty check to set # of removed cells
    if str_difficulty == "easy":
        removed_cells = 30
    elif str_difficulty == "medium":
        removed_cells = 40
    elif str_difficulty == "hard":
        removed_cells = 50
    # Difficulty check to set # of removed cells

    # # BOARD INITIALIZATION # #
    Sudoku = SudokuGenerator(9, removed_cells)  # Board Initialize
    Sudoku.fill_values()  # Fills Board
    Sudoku2 = copy.deepcopy(Sudoku) # Copy of initial board for validation purposes
    generated_board = Sudoku2.get_generated_board() # Copied board
    Sudoku.remove_cells()  # Removes Cells
    altered_generated_Board = Sudoku.get_generated_board()  # Altered Board
    # # BOARD INITIALIZATION # #

    while True:
        # starts a game and waits for the return of game condition
        screen.fill(White)
        game_condition = game_start(str_difficulty)

        # RESET BUTTON NEEDS CODE FOR RESETTING USER'S INPUTTED NUMBERS
        if game_condition == "lost":
            draw_game_over()
        elif game_condition == "win":
            draw_game_win()
        elif game_condition == "reset":
            # RESETS THE BOARD TO BEFORE USER'S ADDED GUESSES
            pass
        elif game_condition == "restart":
            # cv paste of board initialization :P it works ok? <3
            str_difficulty = draw_game_start(screen)
            if str_difficulty == "easy":
                removed_cells = 30
            elif str_difficulty == "medium":
                removed_cells = 40
            elif str_difficulty == "hard":
                removed_cells = 50
            # Difficulty check to set # of removed cells

            # # BOARD INITIALIZATION # #
            Sudoku = SudokuGenerator(9, removed_cells)  # Board Initialize
            Sudoku.fill_values()  # Fills Board
            Sudoku2 = copy.deepcopy(Sudoku)  # Copy of initial board for validation purposes
            generated_board = Sudoku2.get_generated_board()  # Copied board
            Sudoku.remove_cells()  # Removes Cells
            altered_generated_Board = Sudoku.get_generated_board()  # Altered Board
            # # BOARD INITIALIZATION # #