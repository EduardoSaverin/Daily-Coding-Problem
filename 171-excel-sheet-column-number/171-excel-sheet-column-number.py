class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        length = len(columnTitle)
        index = 1
        col_num = 0
        for char in list(columnTitle):
            c_val = ord(char) - ord('A') + 1
            col_num += pow(26, length - index)*c_val
            index += 1
        return col_num