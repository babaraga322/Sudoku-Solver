class Sudoku:
    def __init__(self, board):
        self.board = board
        self.solve()

    def solve(self):
        row, col = self.findUnassigned()
        if (row, col) == (-1, -1):
            return True

        for num in map(str, range(1, 10)):

            if self.isSafe(row, col, num):

                self.board[row][col] = num

                if self.solve():

                    return True
                self.board[row][col] = '.'


    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1

    def isSafe(self, row, col, ch):
        boxrow = row - row % 3
        boxcol = col - col % 3
        if self.checkrow(row, ch) and self.checkcol(col, ch) and self.checksquare(boxrow, boxcol, ch):
            return True
        return False

    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checksquare(self, row, col, ch):
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if self.board[r][c] == ch:
                    return False
        return True






