class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # If you see my solution matches exactly with Climbing Stairs Case Solution
        d = {}
        n = len(cost)
        def recursion(n, d):
            if n < 0:
                return 0
            elif n == 0 or n == 1:
                return cost[n]
            elif n in d:
                return d[n]
            d[n] = cost[n] + min(recursion(n-1, d), recursion(n-2, d))
            return d[n]
        return min(recursion(n-1, d), recursion(n-2,d))