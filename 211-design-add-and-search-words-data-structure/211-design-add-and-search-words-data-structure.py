class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node =  self.root
        index = 0
        while index < len(word):
            if word[index] in node:
                node = node[word[index]]
                index += 1
                continue
            break
        while index < len(word):
            node[word[index]] = {}
            node = node[word[index]]
            index += 1
        node['$'] = {} # Word End Marking

    def search(self, word: str) -> bool:
        return self.recursive_search(word, self.root)
    
    def recursive_search(self, word:str, root):
        if not word and '$' in root:
            return True
        # print('Word', word)
        index = 0
        while index < len(word):
            char = word[index]
            if char == '.':
                result = []
                for key in root.keys():
                    if key != '$':
                        # print('Key', key)
                        result.append(self.recursive_search(word[index+1:], root[key]))
                return any(result)
            elif char not in root:
                return False
            elif char in root:
                root = root[char]
            index += 1
        return True if '$' in root else False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)