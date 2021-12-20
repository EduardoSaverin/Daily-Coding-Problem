class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = index = 0
        total = 0
        result = len(nums)*2 # Dummy Value
        while index < len(nums):
            total += nums[index]
            while total >= target and start < len(nums):
                result = min(result, (index-start+1))
                total -= nums[start]
                start+=1
            index += 1
        return 0 if result == len(nums)*2 else result