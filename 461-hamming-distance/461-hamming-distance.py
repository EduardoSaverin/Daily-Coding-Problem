class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while x!= 0 or y!=0:
            n = x&1
            m = y&1
            if n!=m:
                count += 1
            x = x >> 1
            y = y >> 1
        return count