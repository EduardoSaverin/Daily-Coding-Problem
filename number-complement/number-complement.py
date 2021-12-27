class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num).replace('0b','')
        power = 0
        total = 0
        for char in s[::-1]:
            if char == '0':
                total += pow(2, power)
            power += 1
        return total