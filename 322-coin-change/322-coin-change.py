class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0] = 0
        def recursion(amount):
            if amount in dp:
                return dp[amount]
            dp[amount] = float("inf")
            for coin in coins:
                if amount - coin >= 0 :
                    dp[amount] = min(dp[amount], 1+recursion(amount-coin))
            return dp[amount]
        recursion(amount)
        return -1 if dp[amount] == float("inf") else dp[amount]
            