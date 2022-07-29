class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        final = []
        for word in words:
            d = {}
            visited = set() # To check single mapping
            if len(word) != len(pattern):
                continue
            result = ""
            for index in range(len(pattern)):
                char = word[index]
                if pattern[index] in d:
                    char = d[pattern[index]]
                elif char in visited:
                    break
                else:
                    d[pattern[index]] = char
                    visited.add(char)
                result += char
            if word == result:
                final.append(word)
        return final
