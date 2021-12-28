# 438. Find All Anagrams in a String

## Medium

***

Given two strings `s` and `p`, return _an array of all the start indices of_ `p`_'s anagrams in_ `s`. You may return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

&#x20;

**Example 1:**

```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

**Example 2:**

```
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

&#x20;

**Constraints:**

* `1 <= s.length, p.length <= 3 * 104`
* `s` and `p` consist of lowercase English letters.

```python
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # What a rhyme we got here ana & pana :D
        ana = defaultdict(int)
        pana = defaultdict(int)
        result = []
        length = len(p)
        for char in list(s[:length]):
            ana[char] = ana[char] + 1
        for char in list(p):
            pana[char] = pana[char] + 1
        if ana == pana:
            result.append(0)
        oldIndex = 0
        for index in range(length, len(s)):
            ana[s[oldIndex]] = ana[s[oldIndex]] - 1
            oldIndex += 1
            ana[s[index]] = ana[s[index]] + 1
            # print(oldIndex,ana,pana)
            if self.compare(ana,pana):
                result.append(oldIndex)
        return result
        
    def compare(self, a,b):
        akeys = a.keys()
        for key,value in b.items():
            if a[key] == 0:
                return False
            elif key not in akeys:
                return False
            elif a[key] != b[key]:
                return False
        return True
```
