class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        num = n
        while num != 1:
            if num not in d:
                d[num] = 1
            else:
                return False
            sum_ = 0
            for digit in str(num):
                sum_ += pow(int(digit), 2)
            num = sum_
        return True
            