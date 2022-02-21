class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        result = set()
        for num in nums:
            d[num] += 1
            if d[num] > len(nums)/3:
                result.add(num)
        return result