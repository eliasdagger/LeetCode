# LeetCode 36 - Valid Sudoku (Medium)
#
# Given a 9 x 9 Sudoku board where empty cells are marked '.', decide whether the
# board as it has been filled in so far is valid. Only the cells that already
# contain a digit need to be checked:
#
#   each row must contain the digits 1-9 without repeating
#   each column must contain the digits 1-9 without repeating
#   each of the nine 3 x 3 sub-boxes must contain the digits 1-9 without repeating
#
# A valid board does not have to be solvable, and it does not have to be full - it
# just must not already break any of those three rules.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            visited = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in visited:
                    return False
                visited.add(board[row][i])
        for col in range(9):
            visited = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in visited:
                    return False
                visited.add(board[i][col])
        for square in range(9):
            visited = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j

                    if board[row][col] == ".":
                        continue
                    if board[row][col] in visited:
                        return False
                    visited.add(board[row][col])
        return True