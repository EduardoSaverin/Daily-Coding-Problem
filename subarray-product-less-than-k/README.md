# 713. Subarray Product Less Than K

## Medium

***

Given an array of integers `nums` and an integer `k`, return _the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than_ `k`.

&#x20;

**Example 1:**

```
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
```

**Example 2:**

```
Input: nums = [1,2,3], k = 0
Output: 0
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 3 * 104`
* `1 <= nums[i] <= 1000`
* `0 <= k <= 106`

```python
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
                
```
