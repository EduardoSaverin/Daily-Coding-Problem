class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mem = {}
        MOD = 10**9+7
        def dp(n, target):
            nonlocal k
            if n == 0:
                return 0 if target > 0 else 1
            key = (n, target)
            if key in mem:
                return mem[key]
            total = 0
            for i in range(max(0, target-k), target):
                total += dp(n-1, i)
            mem[key] = total
            return total
        return dp(n, target) % MOD