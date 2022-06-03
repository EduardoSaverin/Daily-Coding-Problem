class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_sum()
        print(self.matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for row in range(row1, row2+1):
            total += (self.matrix[row][col2] - (self.matrix[row][col1-1] if col1 >= 1 else 0))
        return total
    
    def prefix_sum(self):
        for i in range(len(self.matrix)):
            for j in range(1, len(self.matrix[0])):
                self.matrix[i][j] = self.matrix[i][j-1] + self.matrix[i][j]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# 3 3 4 8 10
