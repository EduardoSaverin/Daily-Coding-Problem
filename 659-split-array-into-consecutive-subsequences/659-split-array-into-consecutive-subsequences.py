class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        #.
        occurrences, next_nums = defaultdict(int), defaultdict(int)
        for num in nums:
            occurrences[num] += 1
        for num in nums:
            if occurrences[num] == 0:
                continue 
           
            elif next_nums[num] > 0:
                next_nums[num] -= 1
                next_nums[num + 1] += 1
           
            elif occurrences[num + 1] > 0 and occurrences[num + 2] > 0:
                occurrences[num + 1] -= 1
                occurrences[num + 2] -= 1
                next_nums[num + 3] += 1
            else:
                return False
            occurrences[num] -= 1
        return True
        