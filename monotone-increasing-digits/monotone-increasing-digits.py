class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        string = list(str(n))
        length = len(string)
        startpoint = length
        for index in range(length-1, 0, -1):
            # print('Index', index)
            if string[index-1] > string[index]:
                startpoint = index-1
                num = int(string[index-1])
                # print(num)
                string[index-1] = str(num-1)
        for index in range(startpoint+1, length):
            string[index] = '9'
        # print(string)
        return int(''.join(string))