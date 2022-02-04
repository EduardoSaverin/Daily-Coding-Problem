class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        count = 0
        result = 0
        for index in range(len(nums)):
            count += 1 if nums[index] == 1 else -1
            if count == 0:
                result = max(result, index+1)
            elif count in d:
                result = max(result, index - d[count])
            else:
                d[count] = index
        return result