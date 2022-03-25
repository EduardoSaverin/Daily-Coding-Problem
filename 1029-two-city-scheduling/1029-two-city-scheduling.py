class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        # Tried sorting by A then B, but we need to sort actually by their diff
        # because that represents difference between going to A or B. 
        costs.sort(key=lambda x : x[0]-x[1])
        result = 0
        for A, B in costs[:n]:
            result += A
        for A, B in costs[n:]:
            result += B
        return result
            