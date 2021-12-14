class Solution:
    def reverseBits(self, n: int) -> int:
        value = bin(n).replace("0b", "").zfill(32)
        return int(value[::-1],2)