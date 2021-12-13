class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for bit in bin(n):
            if bit == '1':
                result += 1
        return result