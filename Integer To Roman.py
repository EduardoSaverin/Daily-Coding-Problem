# [LINK] https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {1:'I',2: 'II',3: 'III', 4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        roman = 'I'
        result = ''
        while num != 0:
            if num in romans:
                result += romans[num]
                break
            oldKey = 1
            # print(romans.keys())
            for key in romans.keys():
                if num > key:
                    oldKey = key
                else:
                    break
            print(oldKey)
            num = num - oldKey
            result += romans[oldKey]
            
        return result