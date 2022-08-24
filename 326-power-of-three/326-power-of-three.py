class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (log10(n)/log10(3)).is_integer()