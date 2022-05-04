class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        count = 0
        for index, num in enumerate(nums):
            diff = k - nums[index]
            if (num == diff and d[num] >= 2) or (num != diff and d[num] > 0 and d[diff] > 0):
                d[diff] -= 1
                d[num] -= 1
                count += 1
                
        return count
            