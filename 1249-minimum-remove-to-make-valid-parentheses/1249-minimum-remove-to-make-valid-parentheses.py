class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left_index = []
        right_index = []
        for index, char in enumerate(list(s)):
            if char == "(":
                left_index.append(index)
            elif char == ")":
                if left_index and left_index[-1] < index:
                    left_index.pop()
                else:
                    right_index.append(index)
        array = list(s)
        left_index.extend(right_index)
        return "".join([char for idx, char in enumerate(array) if idx not in left_index])
                
                        