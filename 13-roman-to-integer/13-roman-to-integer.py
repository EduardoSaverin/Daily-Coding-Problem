class Solution:
    def romanToInt(self, s: str) -> int:
        mappings = {'I': 1,'II': 2, 'III': 3, 'IV': 4,'V': 5,'IX': 9,'X': 10,'XL': 40, 'L': 50,'XC': 90,'C': 100,'CD': 400, 'D': 500, 'CM': 900,'M': 1000}
        num = 0
        index = 0
        while index < len(s):
            if index + 1 < len(s):
                if s[index: index+2] in mappings:
                    num += mappings[s[index: index+2]]
                    index = index+2
                else:
                    num += mappings[s[index]]
                    index += 1
            else:
                num += mappings[s[index]]
                index += 1
        return num