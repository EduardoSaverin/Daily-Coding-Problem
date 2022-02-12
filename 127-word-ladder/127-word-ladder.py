from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Got TLE
        # Next improvement can be is to convert wordList from List to Set
        # Since check "if exists" takes linear time in List and Constant in Set
        wordList = set(wordList)
        charSet = {w for word in wordList for w in word}
        queue = deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for index in range(len(word)):
                for char in charSet:
                    new_word = word[:index] + char + word[index+1:]
                    if new_word in wordList:
                        wordList.remove(new_word)
                        queue.append([new_word, length+1])
        return 0