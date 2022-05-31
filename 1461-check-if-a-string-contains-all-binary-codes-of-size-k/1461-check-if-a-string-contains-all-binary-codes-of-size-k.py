class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Total Possible Binary from k
        count = 1 << k
        # We will interate through given binary string s and will note down different binary substrings of length
        # k once we finish iterating if the set() contains equal possible substrings i.e 2^k then True otherwise
        # False
        group = set()
        for index in range(len(s)-k, -1, -1):
            group.add(s[index:index+k])
        return len(group) == count
    