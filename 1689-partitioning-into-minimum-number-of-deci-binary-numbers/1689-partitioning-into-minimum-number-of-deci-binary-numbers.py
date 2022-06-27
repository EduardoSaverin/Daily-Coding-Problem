class Solution:
    def minPartitions(self, n: str) -> int:
        maximum = 0
        for char in list(n):
            maximum = max(maximum, int(char))
        return maximum