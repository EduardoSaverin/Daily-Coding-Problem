class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix[0])):
            matrix[0][i] = int(matrix[0][i])
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
                elif matrix[i][j] != "0":
                    matrix[i][j] = int(matrix[i][j]) + int(matrix[i-1][j])
        result = 0
        for index in range(len(matrix)):
            # print(matrix[index])
            result = max(result, self.max_histogram_rectangle(matrix[index]))
        return result
    
    def max_histogram_rectangle(self, height):
        height.append(0)
        stack = [-1]
        result = 0
        for index in range(len(height)):
            while height[index] < height[stack[-1]]:
                h = height[stack.pop()]
                w = index-1 - stack[-1]
                result = max(result, h*w)
            stack.append(index)
        return result