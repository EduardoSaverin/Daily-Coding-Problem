class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Solving in same way as Longest Substring without repeating chars
        result, index = 0, 0
        d = defaultdict(lambda:-1)
        prefix_sum = self.prefix_sum(nums)
        start = 0
        while index < len(nums):
            start = max(start, d[nums[index]] +1)
            # sum(nums[start : index + 1])
            result = max(result, (prefix_sum[index+1] - prefix_sum[start]))
            d[nums[index]] = index
            index += 1
        return result
    
    def prefix_sum(self, nums):
        result = [0]*(len(nums)+1)
        for index in range(1, len(result)):
            num = nums[index-1]
            result[index] = (num + result[index-1])
        return result
            