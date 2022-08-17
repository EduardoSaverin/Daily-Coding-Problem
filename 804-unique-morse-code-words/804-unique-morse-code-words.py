class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        h = set()
        for word in words:
            s = ''
            for char in list(word):
                index = ord(char) - ord('a')
                s += l[index]
            h.add(s)
        return len(h)