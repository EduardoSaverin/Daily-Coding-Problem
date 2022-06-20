class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie, ans = {}, 0
        for word in words:
            node = trie
            for c in word[::-1]:
                if '$' in node: 
                    ans -= node.pop('$')
                node = node.setdefault(c, {})
            if not node:
                node['$'] = len(word) + 1
                ans += node['$']
        return ans