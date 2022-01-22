class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return self.recursion(n)
    
    @lru_cache(None)
    def recursion(self, n):
        if n == 0:
            return False
        for i in range(1, int(sqrt(n)) + 1):
            if not self.recursion(n-pow(i,2)): # Since We can remove sqaure of numbers
                return True
        return False