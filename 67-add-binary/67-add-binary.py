class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length1 = len(a)
        length2 = len(b)
        if length1 < length2:
            a = '0'*(length2-length1) + a
        else:
            b = '0'*(length1-length2) + b
        index = len(a) - 1
        carry = 0
        arr = []
        while index >= 0:
            carryover1, result = self.add_binary(int(a[index]), int(b[index]))
            carryover2, result = self.add_binary(result, carry)
            arr.append(str(result))
            carry = max(carryover2, carryover1)
            index -= 1
        if carry != 0:
            arr.append(str(carry))
        return ''.join(arr[::-1])
                
            
    def add_binary(self, x,y):
        if x == 0 and y == 0:
            return [0,0]
        elif x == 1 and y == 1:
            return [1,0]
        else:
            return [0,1]