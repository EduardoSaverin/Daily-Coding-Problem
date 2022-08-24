class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and n == 3**round(math.log(n,3))