class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs = 0
        numbers_of_tests = minutesToTest / minutesToDie
        # Why adding one
        # Suppose we need to find one poisonous bucket from 5 buckets if we check 4 buckets and find no position then for sure 5th one is poisonous. Hence adding (+ 1)
        while (numbers_of_tests+1)**pigs < buckets:
            pigs += 1
        return pigs