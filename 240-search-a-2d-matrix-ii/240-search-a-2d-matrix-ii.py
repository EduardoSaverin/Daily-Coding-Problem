class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = 0
        rows = len(matrix)
        cols = len(matrix[0])
        rowes = []
        for i in range(rows):
            if matrix[i][0] <= target <= matrix[i][cols-1]:
                rowes.append(i)
            if matrix[i][0] > target:
                break
        for row in rowes:
            column = bisect.bisect_left(matrix[row], target)
            if matrix[row][column] == target or matrix[row][column-1] == target:
                return True
        return False