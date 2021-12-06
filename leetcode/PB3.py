"""
Given a string s, find the length of the longest substring without repeating characters.
"""
from collections import defaultdict


class Solution:
    # O(n^2)
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        for i in range(0, len(s)):
            chars = set()
            for j in range(i, len(s)):
                if s[j] in chars:
                    break
                else:
                    maximum = max(maximum, j-i+1)
                    chars.add(s[j])
        return maximum

    # O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        d  = defaultdict(lambda:-1)
        i = 0 # Index of last char that is repeated now
        result = 0 # Max Length os Substring
        for index in range(len(s)):
            i = max(i, d[s[index]]+1)
            result = max(result, index-i+1)
            d[s[index]] = index
        return result
