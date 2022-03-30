class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix[0])
        index = -1
        for rowIndex in range(len(matrix)):
            if matrix[rowIndex][0] <= target <= matrix[rowIndex][-1]:
                index = rowIndex
        if index == -1:
            return False
        return self.linear_search(matrix[index], target)
    
    def linear_search(self, nums, target):
        if target in nums:
            return True
        return False