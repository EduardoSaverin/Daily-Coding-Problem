class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def recursion(start, end, path):
            if start == 0 and end == 0:
                result.append(path[:])
            if start > 0:
                recursion(start-1, end, path + '(')
            if end > 0 and end > start:
                recursion(start, end-1, path + ')')
        recursion(n,n,'')
        return result