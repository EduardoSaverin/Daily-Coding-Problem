class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float("inf")
        result = 0
        for price in prices:
            if price < lowest:
                lowest = price
            elif (price-lowest) > result:
                result = price-lowest
        return result