import sys
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # Binary Search
        MOD = 1000000007
        low = 1
        high = sys.maxsize # Python 2 sys.maxint
        lcm = self.lcm(a,b) # So that we calculate it only once
        while low < high:
            mid = low + (high-low) // 2 # Mid of low and high
            # If numbers divisible is < n , it means we have to go up to get close to nth
            if self.termsCount(mid, a, b, lcm) < n:
                low = mid+1
            else:
                high = mid
        return low % MOD
    
    def termsCount(self, num:int, a:int, b:int, lcm:int) -> int:
        # Returns number of nums divisible by a or b
        # Divisible by a + Divisible by b - Divisble by both (to prevent twice counting)
        return (num // a) + (num // b) - (num // lcm)
    
    def gcd(self, a:int, b:int) -> int:
        if a == 0:
            return b
        return gcd(b%a, a)
    
    def lcm(self, a:int, b:int) -> int:
        return a*b // self.gcd(a,b)