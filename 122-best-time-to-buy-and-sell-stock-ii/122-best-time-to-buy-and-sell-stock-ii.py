class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = [0]
        for index in range(1, len(prices)):
            diff.append(prices[index] - prices[index-1])
        result = 0
        for _, value in enumerate(diff):
            if value > 0:
                result += value
        return result