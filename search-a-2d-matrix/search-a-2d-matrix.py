class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        minRow = 0
        maxRow = 0
        for r in range(row):
            if target <= matrix[r][col-1]:
                maxRow = r
            elif matrix[r][0] >= target:
                minRow = r
        for r in range(minRow, maxRow+1):
            for c in range(col):
                if matrix[r][c] == target:
                    return True
        return False
        