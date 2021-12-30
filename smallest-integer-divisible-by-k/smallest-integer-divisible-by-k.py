class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        num = 0
        for i in range(k):
            num = num*10 + 1
            if num%k == 0:
                return len(str(num))
        return -1