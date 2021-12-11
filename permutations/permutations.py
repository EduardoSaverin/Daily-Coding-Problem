from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def recursion(nums, temp, result):
            if not nums:
                result.append(temp)
            for index in range(len(nums)):
                recursion(nums[:index] + nums[index+1:], temp + [nums[index]], result)
        recursion(nums, [], result)
        return result