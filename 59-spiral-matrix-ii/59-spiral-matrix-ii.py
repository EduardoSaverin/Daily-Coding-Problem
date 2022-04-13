class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(0)
            matrix.append(temp)
        startRow , endRow = 0, n-1
        startCol, endCol = 0, n-1
        start = 1
        while startRow <= endRow and startCol <= endCol:
            # Right
            for index in range(startCol, endCol+1):
                matrix[startRow][index] = start
                start += 1
            startRow += 1
            # Down
            for index in range(startRow, endRow+1):
                matrix[index][endCol] = start
                start += 1
            endCol -= 1
            # Left
            for index in range(endCol, startCol-1, -1):
                matrix[endRow][index] = start
                start += 1
            endRow -= 1
            # Up
            for index in range(endRow, startRow-1, -1):
                matrix[index][startCol] = start
                start += 1
            startCol += 1
        return matrix