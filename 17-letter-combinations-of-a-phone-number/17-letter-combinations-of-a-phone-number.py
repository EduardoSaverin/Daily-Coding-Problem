class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
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
        arr = []
        temp = []
        for index, digit in enumerate(list(digits)):
            temp = self.d[digit]
            arr = self.product(temp, arr)
        return arr
    
    def product(self, arr1, arr2):
        if len(arr2) == 0:
            return arr1
        result = []
        for x in arr1:
            for y in arr2:
                result.append(y+x)
        return result
        