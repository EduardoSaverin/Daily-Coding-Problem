from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(p)
        d1 = self.getDict(s[:length])
        d2 = self.getDict(p[:length])
        result = []
        start = 0
        end = length-1
        while end < len(s):
            if self.compare(d1, d2):
                result.append(start)
            end = end + 1
            if end < len(s):
                d1[s[start]] -= 1
                if d1[s[start]] == 0:
                    del d1[s[start]]
                start += 1
                d1[s[end]] += 1
        return result
    
    def getDict(self, s:str):
        d = defaultdict(int)
        for char in list(s):
            d[char] += 1
        return d
    
    def compare(self, d1, d2):
        for key in d2.keys():
            if key not in d2:
                return False
            elif d1[key] != d2[key]:
                return False
        return True