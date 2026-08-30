class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        l = 0
        r = (row * col) - 1

        while  l <= r :
            m = (l + r) // 2

            row = m // col
            cols = m % col

            if matrix [row][cols] == target:
                return True 
            elif matrix [row][cols] < target:
                l = m + 1
            else:
                r = m - 1
        return False
