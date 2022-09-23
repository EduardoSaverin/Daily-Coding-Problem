class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = ""
        MOD = 10**9+7
        for num in range(1, n+1):
            b = bin(num)[2:]
            result += b
        return int(result, 2) % MOD