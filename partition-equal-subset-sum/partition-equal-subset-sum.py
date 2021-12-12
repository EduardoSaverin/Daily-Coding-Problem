class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2
        if total%2 == 1 or len(nums) == 1:
            return False
        d = {}
        def recursion(target, index, d):
            if target < 0 or index == len(nums):
                return False
            elif target == 0:
                return True
            elif (index, target) in d:
                return d[(index, target)]
            value = recursion(target - nums[index], index+1, d) or recursion(target, index+1, d)
            d[(index, target)] = value
            return value
        return recursion(target, 0, d)