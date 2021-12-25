class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def recursion(nums, temp, result):
            if not nums:
                result.append(temp)
            for index in range(len(nums)):
                if index > 0 and nums[index] == nums[index-1]:
                    continue
                recursion(nums[:index] + nums[index+1:], temp + [nums[index]], result)
        recursion(nums, [], result)
        return result