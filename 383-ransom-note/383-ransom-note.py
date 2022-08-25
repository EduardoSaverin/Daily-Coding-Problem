class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counterA = self.getDict(ransomNote)
        counterB = self.getDict(magazine)
        for key in counterA.keys():
            if counterB[key] < counterA[key]:
                return False
        return True
    
    def getDict(self, s: str):
        d = defaultdict(int)
        for char in list(s):
            d[char] += 1
        return d