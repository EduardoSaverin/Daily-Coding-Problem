from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for s in s1:
            d1[s] += 1
        for s in s2[:len(s1)]:
            d2[s] += 1
        i = 0
        j = len(s1)
        while j < len(s2):
            if d1 == d2:
                return True
            d2[s2[i]] -= 1
            if d2[s2[i]] < 1:
                d2.pop(s2[i])
            d2[s2[j]] = d2[s2[j]] + 1
            i += 1
            j += 1
        return d1 == d2
        