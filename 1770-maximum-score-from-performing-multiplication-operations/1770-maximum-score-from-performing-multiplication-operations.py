class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        @lru_cache(2000)
        def dp(left, i):
            if i == m:
                return 0
            l = dp(left+1, i+1) + nums[left]*multipliers[i]
            # l + r == m -> r = m-l
            r = dp(left, i+1) + nums[n - (i-left) - 1]*multipliers[i]
            return max(l,r)
        return dp(0,0)