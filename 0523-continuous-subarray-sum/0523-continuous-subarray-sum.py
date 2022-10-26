class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:0}
        s = 0
        for index, num in enumerate(nums):
            s += num
            if s % k not in d:
                d[s%k] = index+1
            elif d[s%k] < index:
                return True
        return False