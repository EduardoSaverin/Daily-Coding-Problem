class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.counts = [[s.count("0"), s.count("1")] for s in strs]
        return self.dp(m,n,0)
        
    @lru_cache(None)
    def dp(self, m, n, k):
        if m < 0 or n < 0:
            return -float("inf")
        if k == len(self.counts):
            return 0
        x, y = self.counts[k]
        return max(1+self.dp(m-x, n-y, k+1), self.dp(m,n,k+1))
        