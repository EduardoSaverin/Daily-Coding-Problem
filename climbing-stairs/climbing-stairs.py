class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        def recursion(n, d):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            elif n in d:
                return d[n]
            sum = recursion(n-1, d) + recursion(n-2, d)
            d[n] = sum
            return sum
        return recursion(n, d)