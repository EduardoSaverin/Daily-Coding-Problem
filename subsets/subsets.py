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

# Solution 3 : Related to Subsets 2 PB 90         
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def recursion(nums, start, path, result):
            result.append(path[:])
            for index in range(start, len(nums)):
                # if index != start and nums[index] == nums[index-1]:
                #     continue
                path.append(nums[index])
                recursion(nums, index+1, path, result)
                path.pop()
        result = []
        recursion(nums, 0, [], result)
        return result
