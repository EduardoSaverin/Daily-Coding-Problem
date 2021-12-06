"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
"""

from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for index in range(len(s1), len(s2)+1):
            if self.checkPermutation(s1, s2[index-len(s1):index]):
                return True
        return False
        
    
    def checkPermutation(self, s1: str, s2: str) -> bool:
        hashmap = self.getHashmap(s1)
        # print(hashmap)
        for c in list(s2):
            hashmap[c] = hashmap[c] - 1
        # print(hashmap)
        for key in hashmap.keys():
            if hashmap[key] != 0:
                return False
        return True
        
    def getHashmap(self, s1: str):
        d = defaultdict(int)
        for c in list(s1):
            d[c] = d[c] + 1
        return d
        