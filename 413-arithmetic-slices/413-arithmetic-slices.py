class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        total_count = 0
        for index in range(2, len(nums)):
            # (3rd-2nd) == (2nd-1st)
            if nums[index] - nums[index-1] == nums[index-1] - nums[index-2]:
                count += 1
                total_count += count
            else:
                count = 0
        return total_count