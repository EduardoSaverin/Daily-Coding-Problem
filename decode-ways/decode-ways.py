class Solution:
    def numDecodings(self, s: str) -> int:
        # Similar to staircase problem
        arr = [0]*(len(s)+1)
        arr[0] = 1
        arr[1] = 0 if s[0] == '0' else 1
        for index in range(2, len(s)+1):
            # one step
            if 0 < int(s[index-1:index]) <=9:
                arr[index] += arr[index-1]
            if 10 <= int(s[index-2:index]) <= 26:
                arr[index] += arr[index-2]
        return arr[len(s)]
            