# Attempt 1 at a Brute Force solution
# Collected all elements in [cols, rows, boxes] and checked for duplicates

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(n):
            row = [int(board[n][i]) for i in range(9) if board[n][i]!='.']
            # print(f"for {n} row is {row}")
            return len(row) == len(set(row))
        
        def checkCol(n):
            column = [int(board[i][n]) for i in range(9) if board[i][n]!='.']
            # print(f"for {n} column is {column}")
            return len(column) == len(set(column))

        def checkBox(x, y):
            boxContents = [int(board[i][j]) for j in range(y, y+3) for i in range(x, x+3) if board[i][j]!='.']
            # print(f"for {x},{y} box is {boxContents}")
            return len(boxContents) == len(set(boxContents))

        row_col_check = all(checkRow(i) and checkCol(i) for i in range(9))
        box_check = all(checkBox(i, j) for i in (0,3,6) for j in (0,3,6))

        return row_col_check and box_check