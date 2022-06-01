class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        zero = 0
        while zero != len(nums):
            odd, even,zero = 0,0,0
            for index in range(len(nums)):
                # First convert odds to even
                if nums[index] % 2 == 1:
                    odd += 1
                    nums[index] -= 1
                # Check for zero
                if nums[index] == 0:
                    zero += 1
                else:
                    even += 1
                    nums[index] //= 2
            ops += odd
            ops += 1 if even else 0
        return ops