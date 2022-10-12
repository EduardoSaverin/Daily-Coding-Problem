class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)[::-1]
        for index in range(len(nums)-2):
            if nums[index] < nums[index+1] + nums[index+2]:
                return nums[index] + nums[index+1] + nums[index+2]
        return 0