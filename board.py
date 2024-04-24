import pygame
import cell

Black = (0, 0, 0)
White = (255, 255, 255)

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = []

    # Constructor for the Board class.
    # screen is a window from PyGame.
    # difficulty is a variable to indicate if the user chose easy, medium, or hard. Sets # of removed cells.

    # Creating cell objects within the board and attributing/passing their respective values
    # Perhaps instead use set cell value function within cell class?
    def initialize_cells(self, generated_board):
        for row in range(9):
            row_cells = []
            for col in range(9):
                value = generated_board[row][col]  # Check this bullshit out.
                cell_obj = cell.Cell(value, row, col, self.screen)
                row_cells.append(cell_obj)
            self.cells.append(row_cells)

    def draw(self):

        # Calling cell draw function
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()

        # Grid x-axis
        x = 1
        for i in range(1, 10):
            if x % 3 == 0:
                line_width = 8
            else:
                line_width = 3
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (0, i * 100),
                (self.width, i * 100),
                line_width
            )
            x += 1

        # Grid y-axis
        y = 1
        for i in range(1, 9):
            if y % 3 == 0:
                line_width = 8
            else:
                line_width = 3
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (i * 100, 0),
                (i * 100, self.height),
                line_width
            )
            y += 1

    # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
    # Draws every cell on this board.

    def select(self, row, col):
        pass

    # Marks the cell at (row, col) in the board as the current selected cell.
    # Once a cell has been selected, the user can edit its value or sketched value.

    def click(self, x, y):
        pass

    # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
    # of the cell which was clicked. Otherwise, this function returns None.

    def clear(self):
        pass

    # Clears the value cell. Note that the user can only remove the cell values and sketched value that are
    # filled by themselves.

    def sketch(self, value):
        pass

    # Sets the sketched value of the current selected cell equal to user entered value.
    # It will be displayed in the top left corner of the cell using the draw() function.

    def place_number(self, value):
        pass

    # Sets the value of the current selected cell equal to user entered value.
    # Called when the user presses the Enter key.

    def reset_to_original(self):
        pass

    # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).

    def is_full(self):
        pass

    # Returns a Boolean value indicating whether the board is full or not.

    def update_board(self):
        pass

    # Updates the underlying 2D board with the values in all cells.

    def find_empty(self):
        pass

    # Finds an empty cell and returns its row and col as a tuple (x, y).

    def check_board(self):
        pass
    # Check whether the Sudoku board is solved correctly
