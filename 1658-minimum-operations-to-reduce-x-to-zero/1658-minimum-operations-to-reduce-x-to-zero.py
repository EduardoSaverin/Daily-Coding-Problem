class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        return self.minSubArrayLen(nums, sum(nums) - x)
    
    # Smiply using the solution of PB 209
    def minSubArrayLen(self, nums, x):
        index, start, size, total = 0, 0, 0, 0
        found = False
        # Now we will try to get max subarray with matches to the target, because remaining numbers
        # will be the numbers that make x to 0
        while index < len(nums):
            total += nums[index]
            while total > x and start <= index:
                total -= nums[start]
                start += 1
            if total == x:
                found = True
                size = max(size, index-start+1)
            index += 1
        return -1 if not found else len(nums) - size