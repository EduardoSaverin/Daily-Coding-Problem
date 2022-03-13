class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for char in list(s):
            if char in ('}', ']', ')'):
                if len(l) == 0 or not self.check_valid(char, l[-1]):
                    return False
                else:
                    l.pop()
            else:
                l.append(char)
        return False if len(l) != 0 else True
    
    def check_valid(self, char, top):
        if top == '(' and char != ')':
            return False
        elif top == '[' and char != ']':
            return False
        elif top == '{' and char != '}':
            return False
        return True