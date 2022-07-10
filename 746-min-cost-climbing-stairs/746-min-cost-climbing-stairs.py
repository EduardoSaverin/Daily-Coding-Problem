class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = {}
        n = len(cost)
        def recursion(index, total):
            if index < 0:
                return 0
            elif index == 0 or index == 1:
                return cost[index]
            elif index in d:
                return d[index]
            d[index] = cost[index] + min(recursion(index-1, total), recursion(index-2, total))
            return d[index]
        return min(recursion(n-1, 0), recursion(n-2, 0))