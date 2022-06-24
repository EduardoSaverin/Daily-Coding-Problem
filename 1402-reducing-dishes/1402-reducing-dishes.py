class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        total, result = 0, 0
        while satisfaction and total + satisfaction[-1] > 0:
            total += satisfaction.pop()
            result += total
        return result