class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        count = 0
        length = int(math.log(n,10))
        totalDigits = len(digits)
        print(length)
        for index in range(length):
            count += pow(totalDigits, index+1)
        # print(self.numbersWithSameLength(digits,n))
        return count + self.numbersWithSameLength(digits,n)
        
    def numbersWithSameLength(self, digits, n):
        if n < 1:
            return 0
        
        totalDigits = len(digits)
        length = int(math.log(n,10))
        # print('Length', length)
        number = pow(10,length) # if n=20 then number will be 10
        # print('number', number)
        leading_number = n//number
        # print('Leading', leading_number)
        count = 0
        for digit in digits:
            if (int(digit)) < leading_number:
                count += pow(totalDigits, length)
            if (int(digit)) == leading_number:
                    if length == 0:
                        # Single Digit number Case
                        count += 1
                    elif n-(leading_number*number) >= number//10:
                        count += self.numbersWithSameLength(digits, n-(leading_number*number))
            if int(digit) > leading_number:
                return count
        return count