class WordFilter:

    def __init__(self, words: List[str]):
        self.d = defaultdict(lambda:defaultdict(lambda:-1))
        for index, word in enumerate(words):
            for i in range(1, len(word)+1):
                for j in range(len(word)):
                    pre = word[:i]
                    suf = word[j:]
                    self.d[pre][suf] = index
        

    def f(self, prefix: str, suffix: str) -> int:
        return self.d[prefix][suffix]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)