class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = 0 # Total subarrays
        count = 0 # Number of subarrays we get by adding current index element
        for index in range(2, len(nums)):
            if nums[index-1] - nums[index-2] == nums[index] - nums[index-1]:
                count += 1
                total += count
            else:
                count = 0
        return total