class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        sign = None
        length = 1
        for index in range(1, len(nums)):
            if nums[index] > nums[index-1] and sign != True:
                sign = True
                length += 1
            elif nums[index] < nums[index-1] and sign != False:
                sign = False
                length += 1
        return length