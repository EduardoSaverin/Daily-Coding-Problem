class Solution:
    def __init__(self):
        self.dp = {}
        self.dp[0] = 0
        self.dp[1] = 1
        self.dp[2] = 1
    
    def fib(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        return self.fib(n-1) + self.fib(n-2)
        
        