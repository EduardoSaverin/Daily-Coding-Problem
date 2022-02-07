from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # one more letter at a random position
        # This line in question seems wrong because it doesn't allow test case beyond one char diff
        result = ''
        hash1 = self.get_hash(s)
        hash2 = self.get_hash(t)
        for key in hash2.keys():
            if key not in hash1:
                result = result + key*hash2[key]
            elif hash2[key] != hash1[key]:
                result = result + key*(hash2[key]-hash1[key])
        return result
    
    def get_hash(self, s:str):
        d = defaultdict(int)
        for char in s:
            d[char] += 1
        return d