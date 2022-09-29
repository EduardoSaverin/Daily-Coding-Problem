class Solution:
    def palindromePairs(self, words):
        # https://leetcode.com/problems/palindrome-pairs/discuss/2585442/Intuitive-Python3-or-HashMap-or-95-Time-and-Space-or-O(N*W2)
        d, res = dict([(w[::-1], i) for i, w in enumerate(words)]), []
        result = []
        for index, word in enumerate(words):
            if word in d and index != d[word]:
                result.append([index, d[word]])
            if word !="" and "" in d and word==word[::-1]:
                result.append([index,d[""]])
                result.append([d[""],index])
            for j in range(len(word)):
                if word[j:] in d and word[:j] == word[j-1::-1]:
                    result.append([d[word[j:]], index])
                if word[:j] in d and word[j:] == word[:j-1:-1]:
                    result.append([index, d[word[:j]]])
        return result
            