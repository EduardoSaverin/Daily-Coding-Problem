class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Reverse
        left , right = 0, len(matrix)-1
        while left < right:
            matrix[left], matrix[right] = matrix[right], matrix[left]
            left += 1
            right -= 1
        # Transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        