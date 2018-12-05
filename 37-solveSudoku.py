'''
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'

Note:
The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
'''

class Solution:
    def solver(self,board,row,column,block):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(1,10):
                        if k not in row[i] and k not in column[j] and k not in block[(i//3)+(j//3)*3]:
                            board[i][j] = str(k)
                            row[i][k], column[j][k], block[(i//3)+(j//3)*3][k] = 1, 1, 1
                            ans = self.solver(board,row,column,block)
                            if ans:
                                return True
                            else:
                                row[i].pop(k)
                                column[j].pop(k)
                                block[(i//3)+(j//3)*3].pop(k)
                                board[i][j] = '.'
                    return False
        return True
        
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = []
        column = []
        block = []
        for i in range(9):
            row.append({})
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    try:
                        row[i][num]
                    except:
                        row[i][num] = 1
                        
        for j in range(9):
            column.append({})
            for i in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    try:
                        column[j][num]
                    except:
                        column[j][num] = 1
        
        corner = [(0,0),(3,0),(6,0),(0,3),(3,3),(6,3),(0,6),(3,6),(6,6)]
        for k,(cx,cy) in enumerate(corner):
            block.append({})
            for i in range(3):
                for j in range(3):
                    if board[cx+i][cy+j] != '.':
                        num = int(board[cx+i][cy+j])
                        try:
                            block[k][num]
                        except:
                            block[k][num] = 1
        
        self.solver(board,row,column,block)
                            
if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    Solution().solveSudoku(board)
    print(board)