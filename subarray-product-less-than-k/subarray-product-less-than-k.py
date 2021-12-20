class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        start = 0
        index = 0
        count = 0
        while index < len(nums):
            product *= nums[index]
            print('Product', product)
            # If Product goes out of scope then move pointer from left until product is in range
            while product >= k and start < len(nums):
                product = (product//nums[start])
                start += 1
            # If Product is less than k then its elements will be less than K :D
            if product < k:
                count += (index - start + 1)
            index += 1
        return count
        
        
    def numSubarrayProductLessThanKOLD(self, nums: List[int], k: int) -> int:
        # Got TTL With this : O(n^2)
        count = 0
        for index in range(len(nums)):
            product = nums[index]
            if product < k:
                count += 1
            for j in range(index+1, len(nums)):
                product *= nums[j]
                if product < k:
                    count += 1
                else:
                    break
        return count
                