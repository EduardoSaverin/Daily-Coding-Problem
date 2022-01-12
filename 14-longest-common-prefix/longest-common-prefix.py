class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for index in range(len(strs[0])):
            char = strs[0][index]
            for string in strs[1:]:
                if index >= len(string):
                    return prefix
                elif string[:index+1] != strs[0][:index+1]:
                    return prefix
            prefix += char
        return prefix
