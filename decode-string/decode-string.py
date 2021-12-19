class Solution:
    def decodeString(self, s: str) -> str:
        # Let's first find out all string within different []
        # This thing will help us in recursion calling
        closingBracket = {}
        stack = []
        for index, char in enumerate(s):
            if char == '[':
                stack.append(index)
            elif char == ']':
                closingBracket[stack.pop()] = index
        # Uncomment below line to se what we get from above code
        # self.printBracketStrings(s, closingBracket)
        return self.helper(s, 0, len(s)-1, closingBracket)
        
    
    def printBracketStrings(self, s:str, closingBracket):
        for key,value in closingBracket.items():
            print(s[key+1:value])
        
    def helper(self, s, left, right, closingBracket):
        # left and right are boundaries of string within []
        num = 0
        result = []
        while left <= right:
            if s[left].isdigit():
                num = num*10 + int(s[left])
            elif s[left] == '[':
                value = num*self.helper(s, left+1, closingBracket[left] - 1, closingBracket)
                num = 0
                result.append(value)
                left = closingBracket[left]
            else:
                # Simple Characters
                result.append(s[left])
            left += 1
        return "".join(result)