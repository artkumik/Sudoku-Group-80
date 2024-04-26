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
        self.selected_cell = None
        self.board_x = 0
        self.board_y = 0
        self.cell_size = 100
        self.board_area = pygame.Rect(self.board_x, self.board_y, self.width * self.cell_size, self.height * self.cell_size)

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
                line_width = 7
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
        for i in range(1, 10):
            if y % 3 == 0:
                line_width = 7
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
    def get_pos(self):
        mouse_pos = pygame.mouse.get_pos()
        col = mouse_pos[0] // 100
        row = mouse_pos[1] // 100
        return col, row


    def b_select(self, col, row):
        current_cell = self.cells[row][col]
        if current_cell.value == 0:
            if self.selected_cell == current_cell:
                current_cell.deselect()
                self.selected_cell = None

            else:
                if self.selected_cell:
                    self.selected_cell.deselect()
                current_cell.c_select()
                self.selected_cell = current_cell

            if self.selected_cell is not None:
                self.selected_cell.draw()
            else:
                self.draw()

    # Marks the cell at (row, col) in the board as the current selected cell.
    # Once a cell has been selected, the user can edit its value or sketched value.

    def click(self, x, y):
        row = y * 100
        col = x * 100
        return row, col

    # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
    # of the cell which was clicked. Otherwise, this function returns None.

    def clear(self):
        pass

    # Clears the value cell. Note that the user can only remove the cell values and sketched value that are
    # filled by themselves.

    def sketch(self, value):

        if self.selected_cell is not None and self.selected_cell.value == 0:
            if self.selected_cell.sketch != 0 and value != self.selected_cell.sketch:
                self.selected_cell.sketch = 0
                self.selected_cell.draw()

            if self.selected_cell and 1 <= value <= 9:
                self.selected_cell.sketch = value
                print(f"Sketched {value} on cell at ({self.selected_cell.row}, {self.selected_cell.col}).") # DEBUG
                self.selected_cell.draw()
                self.selected_cell.deselect()
                self.selected_cell = None
                self.draw()

    # Sets the sketched value of the current selected cell equal to user entered value.
    # It will be displayed in the top left corner of the cell using the draw() function.

    def place_number(self, value):
        pass

    # Sets the value of the current selected cell equal to user entered value.
    # Called when the user presses the Enter key.


    # Already have a get board method from generator
    # def reset_to_original(self):
    #     pass

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

    def print_board(self):
        for row in self.cells:
            row_values = [cell.value for cell in row]
            print(row_values)
