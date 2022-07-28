class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = self.getHashmap(s)
        d2 = self.getHashmap(t)
        if len(d1) == len(d2):
            for key,count in d1.items():
                if d2[key] != count:
                    return False
            return True
        return False
        
    def getHashmap(self, s:str):
        d = defaultdict(int)
        for char in list(s):
            d[char] = d[char] + 1
        return d
    
        
