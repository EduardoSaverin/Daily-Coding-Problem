class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        charSet = {w for word in wordList for w in word}
        level = {}
        level[beginWord] = [[beginWord]]
        while level:
            new_level = defaultdict(list)
            for word, paths in level.items():
                if word == endWord:
                    return paths
                for index in range(len(word)):
                    for char in charSet:
                        new_word = word[:index] + char + word[index+1:]
                        if new_word in wordList:
                            for path in paths:
                                new_level[new_word].append(path + [new_word])
            wordList = wordList - set(new_level.keys())
            level = new_level
                            