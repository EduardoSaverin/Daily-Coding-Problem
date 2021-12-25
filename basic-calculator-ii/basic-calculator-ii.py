class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        sign = "+"
        for index in range(len(s)):
            char = s[index]
            if char.isdigit():
                num = num*10 + int(char)
            if char in ["+", "-", "*", "/"] or index == len(s)-1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    temp = stack.pop()
                    stack.append(int(temp/num))
                num = 0
                sign = char
        return sum(stack)