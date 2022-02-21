class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        majority = None
        for num in nums:
            d[num] += 1
            if d[num] > len(nums)/2:
                majority = num
        return majority