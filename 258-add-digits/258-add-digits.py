class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        number_of_digits = int(math.log10(num))+1
        while number_of_digits != 1:
            total = 0
            while num != 0:
                digit = num % 10
                num = int(num/10)
                total = total + digit
            num = total
            number_of_digits = int(math.log10(num))+1
        return num