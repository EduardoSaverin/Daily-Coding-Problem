class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Same as PB 476 : https://leetcode.com/problems/number-complement/
        if n == 0:
            return 1
        bit = 1
        while bit <= n:
            bit = bit << 1
        return (bit-1) ^ n