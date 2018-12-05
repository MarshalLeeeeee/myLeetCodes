class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        record = defaultdict(int)
        for i in range(9):
            record.clear()
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if not record[num]:
                        record[num] += 1
                    else:
                        return False
        
        for j in range(9):
            record.clear()
            for i in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if not record[num]:
                        record[num] += 1
                    else:
                        return False
        
        corner = [(0,0),(3,0),(6,0),(0,3),(3,3),(6,3),(0,6),(3,6),(6,6)]
        for cx,cy in corner:
            record.clear()
            for i in range(3):
                for j in range(3):
                    if board[cx+i][cy+j] != '.':
                        num = int(board[cx+i][cy+j])
                        if not record[num]:
                            record[num] += 1
                        else:
                            return False
        return True
            
if __name__ == '__main__':
    print(Solution().isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))