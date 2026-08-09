class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen =set()
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
                
        for i in range(9):
            seen =set()
            for j in range(9):
                cell = board[j][i]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
                
        for row in range (0,9,3):
            for col in range(0,9,3):
                seen = set()                
                for r in range(3):
                    for c in range (3):
                        cell = board [row + r][col + c]                        
                        if cell == ".":
                            continue
                        if cell in seen:    
                            return False
                        seen.add(cell)
        return True                         