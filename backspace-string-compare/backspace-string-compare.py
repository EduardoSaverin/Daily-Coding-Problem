class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        str1 = []
        str2 = []
        for char in list(s):
            if char == '#':
                if str1:
                    str1.pop()
            else:
                str1.append(char)
        for char in list(t):
            if char == '#':
                if str2:
                    str2.pop()
            else:
                str2.append(char)
        print(str1, str2)
        return str1 == str2