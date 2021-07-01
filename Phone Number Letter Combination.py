# [LINK] https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }
        results = []
        for digit in digits:
            temp = []
            if not results:
                temp = (list(hashmap[digit]))
            else:
                for character in hashmap[digit]:
                    for ch in results:
                        temp.append(ch+character)
            results = temp
        return results
        