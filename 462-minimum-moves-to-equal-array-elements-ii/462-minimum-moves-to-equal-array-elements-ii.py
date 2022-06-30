class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        median = 0
        if len(nums) % 2 == 0:
            median = (nums[n//2-1] + nums[n//2]) // 2
        else:
            median = nums[n//2]
        result = 0
        for num in nums:
            result += abs(median - num)
        return result