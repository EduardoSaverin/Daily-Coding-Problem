class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.dfs(s, 0, result, [])
        return result
    
    def dfs(self,string, start= 0, result = [], l = []):
        if start >= len(string):
            result.append(l[:])
        for index in range(start, len(string)):
            if self.plaindrome(string[start:index+1]):
                l.append(string[start:index+1])
                self.dfs(string, index+1, result, l)
                l.pop()

    def plaindrome(self, string):
        return string == string[::-1]