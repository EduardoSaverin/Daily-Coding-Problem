from collections import defaultdict
class Solution:
    # O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        d = self.get_hashmap(nums)
        for num in nums:
            if (num-1) in d:
                continue
            else:
                count = 1 # One Because this number already counted
                number = num # temp variable
                # Run loop till next number in sequence exists
                while (number+1) in d:
                    number += 1
                    count += 1
                result = max(result,count)
        return result
        
    def get_hashmap(self, nums):
        d = defaultdict(int)
        for num in nums:
            d[num] = d[num] + 1
        return d

    # O(nlogn)
    def longestConsecutiveOld(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        index = 0
        maxLength = -1
        count = 1
        # print('Sorted', nums)
        while index < len(nums)-1:
            if nums[index+1] == nums[index]:
                index += 1
            elif nums[index+1] == nums[index]+1:
                count += 1
                index += 1
            else:
                maxLength = max(maxLength, count)
                count = 1
                index += 1
        maxLength = max(maxLength, count)
        return maxLength
