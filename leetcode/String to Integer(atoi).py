class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        res = 0
        index = 0
        negative = 1
        # Skip All WhiteSpaces
        while index < len(s) and s[index] == ' ':
            index += 1

        # Iterate through all negative sign and store negative for later
        if index < len(s) and s[index] == '-':
            index += 1
            negative = -1
        # Skip all positive sings
        elif index < len(s) and s[index] == '+':
            index += 1

        # Gather all number
        checker = set('0123456789')
        while index < len(s) and s[index] in checker:
            res = res*10 + int(s[index])
            index += 1

        # apply the negative sign on the calculated number
        res = res*negative

        # if integer is out of range
        if res < 0:
            return max(res, MIN_INT)
        return min(res, MAX_INT)
