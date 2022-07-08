class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = {}
        
        def dfs(index, target, prev_color):
            key = (index, target, prev_color)
            if index == len(houses) or target < 0 or (m - index) < target:
                return 0 if target == 0 and index == len(houses) else float("inf")
            if key not in dp:
                if houses[index] == 0:
                    # House not colored
                    dp[key] = min(dfs(index+1, target - (new_color != prev_color), new_color) + cost[index][new_color-1] for new_color in range(1, n+1))
                else:
                    # House already colored
                    dp[key] = dfs(index+1, target - (houses[index] != prev_color), houses[index])
            return dp[key]
        result = dfs(0, target, -1)
        return result if result < float("inf") else -1
            