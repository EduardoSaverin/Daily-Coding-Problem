class Solution:
    def minDeletions(self, s: str) -> int:
        d = self.getFrequencies(s)
        freq = list(d.values())
        result = 0
        for index in range(len(freq)):
            f = freq[index]
            while f > 0 and f in (freq[:index] + freq[index+1:]):
                f -= 1
                result += 1
            freq[index] = f
        return result
    
    def getFrequencies(self, s:str):
        d = defaultdict(int)
        for char in list(s):
            d[char] += 1
        return d