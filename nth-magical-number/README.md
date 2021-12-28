# 878. Nth Magical Number

## Hard

***

A positive integer is _magical_ if it is divisible by either `a` or `b`.

Given the three integers `n`, `a`, and `b`, return the `nth` magical number. Since the answer may be very large, **return it modulo** `109 + 7`.

&#x20;

**Example 1:**

```
Input: n = 1, a = 2, b = 3
Output: 2
```

**Example 2:**

```
Input: n = 4, a = 2, b = 3
Output: 6
```

**Example 3:**

```
Input: n = 5, a = 2, b = 4
Output: 10
```

**Example 4:**

```
Input: n = 3, a = 6, b = 4
Output: 8
```

&#x20;

**Constraints:**

* `1 <= n <= 109`
* `2 <= a, b <= 4 * 104`

```python
import sys
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # Binary Search
        MOD = 1000000007
        low = 1
        high = sys.maxsize # Python 2 sys.maxint
        lcm = self.lcm(a,b) # So that we calculate it only once
        # Performing Binary Search
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
```
