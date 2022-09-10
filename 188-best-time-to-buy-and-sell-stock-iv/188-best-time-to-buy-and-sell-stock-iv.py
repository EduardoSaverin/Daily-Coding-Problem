class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        #.
        length = len(prices)
        if length == 0:
            return 0
        max_profit = 0
        if k >= length / 2:
            for i in range(1, length):
                max_profit += max(prices[i] - prices[i-1], 0)
            return max_profit
        
        dp = [[0 for j in range(length)] for i in range(k+1)]
        for i in range(1, k+1):
            maxpr = -prices[0]
            for j in range(1, length):
                dp[i][j] = max( dp[i][j-1], maxpr + prices[j] )
                maxpr = max( maxpr, -prices[j] + dp[i-1][j] )
        return dp[-1][-1]
            