class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = "123456789"
        #rows
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[i][j] in nums and board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
        
        #cols
        cols_mat = [[board[i][j] for i in range(len(board))] for j in range(len(board))]
        
        for i in range(len(cols_mat)):
            seen = set()
            for j in range(len(cols_mat)):
                if cols_mat[i][j] in nums and cols_mat[i][j] in seen:
                    return False
                else:
                    seen.add(cols_mat[i][j])
        # 3x3
        for a in range(3):
            for b in range(3):
                seen = set()
                for c in range(a*3, a*3 + 3):
                    for d in range(b*3, b*3 + 3):
                        if board[c][d] in nums and board[c][d] in seen:
                            return False
                        else:
                            seen.add(board[c][d])
        return True
                    

                
        