class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x : len(x))
        # print(words)
        self.chains = defaultdict(int)
        self.d = {}
        for word in words:
            self.d[word] = 1
        self.longest = 1
        for word in words[::-1]:
            self.dfs(word)
        # print(self.chains)
        return self.longest
            
    
    def dfs(self, word, length = 1):
        # print(word, length)
        if word in self.chains:
            return self.chains[word]
        for index in range(len(word)):
            new_word = word[:index] + word[index+1:]
            if new_word in self.d:
                self.dfs(new_word, length+1)
        self.chains[word] = max(self.chains[word], length)
        self.longest = max(self.longest, length)
        return length