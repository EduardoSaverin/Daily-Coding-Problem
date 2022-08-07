class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        # From Question find mapping
        """
        a -> e,i,u
        e -> a,i
        i -> e,o
        o -> i
        u -> o,i
        """
        a,e,i,o,u = [1]*5
        for _ in range(n-1):
            a,e,i,o,u = e+i+u, a+i, e+o, i, o+i
        return (a+e+i+o+u) % MOD