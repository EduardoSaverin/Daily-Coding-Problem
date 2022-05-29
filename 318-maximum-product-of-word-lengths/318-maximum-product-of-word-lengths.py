class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bits = [0]*len(words)
        for index, word in enumerate(words):
            for char in list(word):
                # Here we are simply record occurence of each char in bit place
                # For Example "a" will set 0001 "b" will set 0010, each character will set its own place in 
                # 26 length bit array and when we perform AND operation we will get 0 if no character matches.
                bits[index] |= (1 << (ord(char) - ord('a')))
        product = 0
        for i in range(len(words)):
            for j in range(i, len(words)):
                if (bits[i] & bits[j]) == 0 and len(words[i])*len(words[j]) > product:
                    product = len(words[i])*len(words[j])
        return product