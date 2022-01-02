class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # For 0 amount there are 0 ways hence first element is zero
        arr = [0] + [float('inf')]*amount
        for amt in range(1, amount+1):
            for coin in coins:
                if amt-coin >= 0:
                    arr[amt] = min(arr[amt], arr[amt-coin] + 1)
        return -1 if arr[-1] == float("inf") else arr[-1]