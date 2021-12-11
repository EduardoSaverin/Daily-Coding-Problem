class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = s.lower()
        result = set()
        def recursion(s, ele, start, result):
            if start >= len(s):
                result.add(ele)
                return
            for index in range(start, len(s)):
                recursion(s, ele[:index] + ele[index].upper() + ele[index+1:], index+1, result)
                recursion(s, ele, index+1, result)
        recursion(s,s,0, result)
        return list(result)