class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = words
        self.stream = ''
        self.trie = TrieTree()
        for word in words:
            self.trie.insert(word[::-1])
        
    def query(self, letter: str) -> bool:
        self.stream += letter
        return self.trie.isPrefix(self.stream[::-1])
    
    
class TrieTree(object):
    def __init__(self) -> None:
        super().__init__()
        self.root = {}
    
    def insert(self, word: str) -> None:
        node = self.root
        index = 0
        # Find Last Node of this word
        while index < len(word):
            if word[index] in node:
                node = node[word[index]]
                index += 1
                continue
            break
        # still some words left -> insert those in trie now
        while index < len(word):
            node[word[index]] = {}
            node = node[word[index]]
            index += 1
        # Word End Marking Character $
        node['$'] = {}
        return

    def isPrefix(self, word: str) -> bool:
        node = self.root
        for character in word:
            if character not in node:
                return False
            if "$" in node[character]:
                return True
            node = node[character]
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)