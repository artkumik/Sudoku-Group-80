import pygame
import cell

Black = (0, 0, 0)
White = (255, 255, 255)

class Board:
    def __init__(self, width, height, screen, difficulty, master_board):
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
        self.master_board = master_board



    def initialize_cells(self, generated_board):
        for row in range(9):
            row_cells = []
            for col in range(9):
                value = generated_board[row][col]
                cell_obj = cell.Cell(value, row, col, self.screen)
                row_cells.append(cell_obj)
            self.cells.append(row_cells)
    # Creating cell objects within the board and attributing/passing their respective values

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
        if row >= len(self.cells) or col >= len(self.cells[0]):
            return None
        return col, row
    # Returns position of cell


    def b_select(self, col, row):
        current_cell = self.cells[row][col]
        if current_cell.value == 0 or current_cell.user_value != 0:
            if self.selected_cell != current_cell:
                self.draw()
                if self.selected_cell:
                    self.selected_cell.deselect()
                    self.selected_cell.draw()
                    self.draw()
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
    # Unused.
    # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
    # of the cell which was clicked. Otherwise, this function returns None.


    def clear(self):
        if self.selected_cell is not None and (self.selected_cell.user_value != 0 or self.selected_cell.sketch != 0):
            self.selected_cell.user_value = 0
            self.selected_cell.sketch = 0
            self.selected_cell.draw()
            print(f'Cell at ({self.selected_cell.row}, {self.selected_cell.col}) has been cleared.') # DEBUG
    # Clears the value cell. Note that the user can only remove the cell values and sketched value that are
    # filled by themselves.


    def sketch(self, value):
        if self.selected_cell is not None and self.selected_cell.value == 0:
            if self.selected_cell.sketch != 0 and value != self.selected_cell.sketch:
                self.selected_cell.sketch = 0
                self.selected_cell.draw()
            if self.selected_cell and 1 <= value <= 9:
                self.selected_cell.sketch = value
                print(f"Sketched {value} on cell at ({self.selected_cell.row + 1}, {self.selected_cell.col + 1}).") # DEBUG
                self.selected_cell.draw()
    # Sets the sketched value of the current selected cell equal to user entered value.
    # It will be displayed in the top left corner of the cell using the draw() function.


    def place_number(self):
        if self.selected_cell is not None and self.selected_cell.sketch != 0:
            self.selected_cell.user_value = self.selected_cell.sketch
            print(f'Placed {self.selected_cell.user_value} on cell at ({self.selected_cell.row + 1}, {self.selected_cell.col + 1})') # DEBUG
            self.selected_cell.sketch = 0
            self.selected_cell.draw()
            self.selected_cell.deselect()
            self.selected_cell = None
            self.draw()
    # Sets the value of the current selected cell equal to user sketched value.
    # Called when the user presses the Enter key.


    def is_full(self):
        updated_board = self.update_board()
        for row in updated_board:
            if 0 in row:
                print('No Full') # DEBUG
                return False
        print('Kirby Full') # DEBUG
        return True
    # Returns a Boolean value indicating whether the board is full or not.


    def update_board(self):
        updated_board = [[0 for _ in range(9)] for _ in range(9)]
        for row_idx, row in enumerate(self.cells):
            for col_idx, cell in enumerate(row):
                if cell.user_value != 0:
                    updated_board[row_idx][col_idx] = cell.user_value
                else:
                    updated_board[row_idx][col_idx] = cell.value
        return updated_board
    # Updates the underlying 2D board with the values in all cells.


    def is_board_equal_to_master(self):
        updated_board = self.update_board()
        for row_idx, row in enumerate(updated_board):
            for col_idx, value in enumerate(row):
                if value != self.master_board[row_idx][col_idx]:
                    return False
        print('Yes, ya boi is equal. ') # DEBUG
        return True
    # Guess


    def check_board(self):
        if self.is_full() and self.is_board_equal_to_master():
            print('You did it') # DEBUG
            return True
        print('No') # DEBUG
        return False
    # Unused atm
    # Checks whether the Sudoku board is solved correctly



    def print_board(self):
        for row in self.cells:
            row_values = [cell.value for cell in row]
            print(row_values)
    # DEBUG print function.