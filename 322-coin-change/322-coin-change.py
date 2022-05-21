class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")]*amount
        for coin in coins:
            for a in range(coin, amount+1):
                dp[a] = min(dp[a], dp[a-coin]+1)
        return -1 if dp[-1] == float("inf") else dp[-1]               