class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = []
        def recursion(nums, index, result):
            nonlocal l
            if index >= len(nums):
                # print(result)
                l.append(result)
            for i in range(index, len(nums)):
                result.append(nums[i])
                recursion(nums, i+1, result[:])
                result.pop()
                recursion(nums, i+1, result[:])
        recursion(nums, 0, [])
        return set(tuple(row) for row in l)
    
    
# Faster Solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums ,[], result)
        return result
    
    def dfs(self, nums, path, result):
        result.append(path[:])
        for index in range(len(nums)):
            self.dfs(nums[index+1:], path + [nums[index]], result)
