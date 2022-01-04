class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        index = 0
        maxLength = -1
        count = 1
        # print('Sorted', nums)
        while index < len(nums)-1:
            if nums[index+1] == nums[index]:
                index += 1
            elif nums[index+1] == nums[index]+1:
                count += 1
                index += 1
            else:
                maxLength = max(maxLength, count)
                count = 1
                index += 1
        maxLength = max(maxLength, count)
        return maxLength