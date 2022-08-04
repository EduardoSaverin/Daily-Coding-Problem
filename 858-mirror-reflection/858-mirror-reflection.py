class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        m, n = 1,1
        while m*p != n*q:
            n += 1
            m = n*q // p
        if n % 2 == 1 and m % 2 == 0:
            return 0
        if n % 2 == 1 and m % 2 == 1:
            return 1
        if n % 2 == 0 and m % 2 == 1:
            return 2
        return -1