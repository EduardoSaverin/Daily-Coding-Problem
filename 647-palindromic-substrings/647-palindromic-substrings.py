class Solution:
    def countSubstrings(self, s: str) -> int:
        # Using Same Solution as in PB5 : Longest Palindrome Substring
        dp = [[False]*len(s) for _ in range(len(s))]
        count = 0
        for index in range(len(s)):
            dp[index][index] = True
            count += 1 # Each Character itself is substring
        for i in range(len(s)-1, -1 , -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if (j-i) == 1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        count += 1
        return count
            