class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in map(int, list(num)):
            while stack and k > 0 and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        while k > 0 and stack:
            stack.pop()
            k -= 1
        if not stack:
            return '0'
        num = ''.join(map(str, stack))
        index = 0
        ptr = 0
        while index < len(num) and num[index] == '0':
            ptr += 1
            index += 1
        return "0" if ptr == len(num) else num[ptr:]