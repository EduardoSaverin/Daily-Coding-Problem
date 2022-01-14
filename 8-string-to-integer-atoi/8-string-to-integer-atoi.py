class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        res = 0
        index = 0
        negative = False
        # Skip All WhiteSpaces
        while index < len(s) and s[index] == ' ':
            index += 1
            
        if index < len(s) and s[index] == '-':
            index += 1
            negative = True
        elif index < len(s) and s[index] == '+':
            index += 1

        # Gather all number
        checker = set('0123456789')
        while index < len(s) and s[index] in checker:
            res = res*10 + int(s[index])
            index += 1

        # apply the negative sign on the calculated number
        if negative:
            res = res*-1

        # if integer is out of range
        if res < 0:
            return max(res, MIN_INT)
        return min(res, MAX_INT)
