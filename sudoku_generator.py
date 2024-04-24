import random
import math

class SudokuGenerator:
    def __init__(self,row_length,removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = self.get_board()
        self.box_length	= int(math.sqrt(self.row_length))

    def get_board(self):
        return [[0 for _ in range(self.row_length)] for _ in range(self.row_length)]
    
    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self,row,num):
        if num in self.board[row]:   
            return False
        else:
            return True
        
    def valid_in_col(self,col,num):
        for i in range(self.row_length):
            if num == self.board[i][col]:
                return False
        return True
    
    def valid_in_box(self,row_start,col_start,num):
        for y in range(3):
            for x in range(3):
                if num == self.board[row_start + y][col_start+x]:
                    return False
        return True
    
    def is_valid(self, row, col, num):
        if self.valid_in_col(col,num)==True and self.valid_in_row(row,num)==True and self.valid_in_box((row//3)*3,(col//3)*3,num)==True:
            return True
        else:
            return False


    def fill_box(self,row_start,col_start):
        unused_in_box = [1,2,3,4,5,6,7,8,9]
        for y in range(3):
            for x in range(3):
                curr_rand = random.randint(0, len(unused_in_box)-1)
                self.board[row_start + y][col_start+x] = unused_in_box.pop(curr_rand)

    def fill_diagonal(self):
        self.fill_box(0,0)
        self.fill_box(3,3)
        self.fill_box(6,6)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False
    
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
        return self.board # <--- Added Return

    def remove_cells(self):
        #removed cells is the amount of cells to removed? can be changed by setup
        size = self.row_length * self.row_length
        remove = random.sample(range(size), self.removed_cells)
        for i in remove:
            remove_row = i // 9
            remove_col = i % 9
            self.board[remove_row][remove_col] = 0

    def get_generated_board(self):  # Added to directly feed generated_board into board class without alterations.
        return self.board

b1 = SudokuGenerator(9,30)


# b1.fill_values()
# b1.print_board()
# print()
# b1.remove_cells()
# b1.print_board()
# print()
# print(b1.get_generated_board())
