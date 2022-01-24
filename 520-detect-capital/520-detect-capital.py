class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        one_small = False
        one_caps = False
        first_capital = True
        for index, char in enumerate(word):
            if index == 0 and char.isupper():
                first_capital = True
            elif char.isupper() and one_small:
                return False
            elif char.islower() and one_caps:
                return False
            elif char.islower():
                one_small = True
            elif char.isupper():
                one_caps = True
        return True