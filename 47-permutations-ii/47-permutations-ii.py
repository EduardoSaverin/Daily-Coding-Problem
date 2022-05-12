class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def recursion(nums, path, result):
            if not nums:
                result.append(path[:])
                return
            for index in range(len(nums)):
                if index > 0 and nums[index] == nums[index-1]:
                    continue
                recursion(nums[:index] + nums[index+1:], path + [nums[index]], result)
        result = []
        recursion(nums, [], result)
        return result