class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(1, n+1):
            for j in range(1, i+1):
                if i+j <= n:
                    print("(dp[i]:",dp[i],",i:",i,")")
                    print("(dp[j]:",dp[j],",j:",j,")")
                    dp[i+j] = max(max(dp[i],i)*max(dp[j],j), dp[i+j])
                    print("->", dp[i+j])
                    print("="*10)
        return dp[n]