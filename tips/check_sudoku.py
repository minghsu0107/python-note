class Solution(object):
    def isValidSudoku(self, board):

        row = {}
        col = {}
        block = {}
        for i, x in enumerate(board):
            for j, y in enumerate(x):
                if y != ".":
                    if (i,y) in row or (j,y) in col or (i/3,j/3,y) in block:
                        return False
                    else:
                        row[i,y] = 1 # row[(i, y)] = 1
                        col[j,y] = 1
                        block[i/3,j/3,y] = 1
        return True