class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False for _ in range(9)] for _ in range(9)]
        col = [[False for _ in range(9)] for _ in range(9)]
        sub = [[False for _ in range(9)] for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue

                num = int(num) - 1
                subIdx = ((r // 3) * 3) + (c // 3)
                if row[r][num] or col[c][num] or sub[subIdx][num]:
                    return False
                
                row[r][num] = col[c][num] = sub[subIdx][num] = True
        
        return True
                


        

        