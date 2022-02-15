class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = nums[0]
        for num in nums[1:]:
            number = number ^ num
        return number