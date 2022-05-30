class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = dividend
        sign = 1
        if (dividend < 0 or divisor< 0) and not (dividend < 0 and divisor< 0):
                sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        # if dividend
        quotient = 0
        temp = 1
        while dividend >= divisor:
            divisor = divisor << 1
            temp = temp << 1
        while temp > 1:
            divisor  = divisor >> 1
            temp = temp >> 1
            if dividend >= divisor:
                dividend -= divisor
                quotient += temp
        if quotient*sign >= 2147483648:
            return 2147483647
        elif quotient*sign <= -2147483648:
            return -2147483648
        else:
            return (quotient)*sign