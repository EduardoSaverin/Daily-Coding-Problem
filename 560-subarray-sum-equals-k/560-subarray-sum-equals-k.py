class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = collections.Counter()
        counter[0] = 1 # Simple denotion that sum == k
        count = 0
        s = 0
        for num in nums:
            s += num
            count += counter[s-k]
            counter[s] += 1
        return count
            