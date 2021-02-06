# LINK https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        hashmap = {}
        for i in range(1, numRows+1):
            hashmap.update({i: ''})
        index = 0
        length = len(s)
        i=0
        if (numRows == 1):
            return s
        while index < length:
            # Move Down
            for i in range(i+1, numRows+1):
                if index < length:
                    hashmap[i] = (hashmap[i] + s[index])
                    index += 1
            
            #Move UP
            for i in range(i-1, 0, -1):
                if index < length:
                    hashmap[i] = (hashmap[i]+ s[index])
                    index += 1
        result = ''
        for i in range(1, numRows+1):
            result += hashmap.get(i)
        return result