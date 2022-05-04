class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        result = 0
        for num in counter:
            result += min(counter[num], counter[k-num])
        return result//2
            