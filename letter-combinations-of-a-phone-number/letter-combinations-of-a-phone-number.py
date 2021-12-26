class Solution:
    def __init__(self):
        self.d = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }
    
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        else:
            arr1 = []
            index = 0
            while index < len(digits):
                arr2 = self.d[digits[index]]
                arr1 = self.crissCross(arr1, arr2)
                index += 1
            return arr1
                
                
    def crissCross(self, arr1, arr2):
        if len(arr1) == 0:
            return arr2
        result = []
        for char1 in arr1:
            for char2 in arr2:
                result.append(char1+char2)
        return result
            
            
        