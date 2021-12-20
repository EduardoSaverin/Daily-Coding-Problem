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