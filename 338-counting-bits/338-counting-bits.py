class Solution:
    # O(nlogn)
    def countBits(self, n: int) -> List[int]:
        result = []
        for num in range(n+1):
            count = self.bit_count(num)
            result.append(count)
        return result
    
    def bit_count(self, n: int) -> int:
        count = 0
        while n != 0:
            count = count + (n&1)
            n = n >> 1
        return count