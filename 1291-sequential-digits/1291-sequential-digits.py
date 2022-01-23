class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        self.low = low
        self.high = high
        self.result = []
        low_digit_count = int(math.log10(low)) + 1 # Lowest Length of num
        high_digit_count = int(math.log10(high)) + 1 # Highest length of num
        for digit in range(low_digit_count, high_digit_count+1):
            self.make(digit, 1, 10, 0)
        return (self.result)
                
    def make(self, digit, start_digit, end_digit, num):
        # We are making number from left to right
        if num > self.high:
            return
        if digit == 0 and num >= self.low and num <= self.high:
            # print('->', num)
            self.result.append(num)
            return
        for i in range(start_digit, min(10, end_digit)):
            # This loop picks each digit of each num from left to right
            # Then calls up same function with one less length and next digit higher than previous
            # print(i)
            num += i*pow(10, digit-1)
            # print(num)
            self.make(digit-1, i+1, i+2, num)
            num = 0
            
        
            