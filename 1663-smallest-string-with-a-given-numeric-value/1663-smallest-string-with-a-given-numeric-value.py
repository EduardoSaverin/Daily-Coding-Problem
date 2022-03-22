class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = []
        for index in range(n):
            # print(26*(n-index-1))
            id = max(k - 26*(n-index-1), 1)
            result.append(chr(97 + id - 1))
            k -= id
        return ''.join(result)