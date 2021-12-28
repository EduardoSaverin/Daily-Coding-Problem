# 34. Find First and Last Position of Element in Sorted Array

## Medium

***

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

&#x20;

**Example 1:**

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

**Example 2:**

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

**Example 3:**

```
Input: nums = [], target = 0
Output: [-1,-1]
```

&#x20;

**Constraints:**

* `0 <= nums.length <= 105`
* `-109 <= nums[i] <= 109`
* `nums` is a non-decreasing array.
* `-109 <= target <= 109`

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        minIndex = self.findMinIndex(nums, target)
        maxIndex = self.findMaxIndex(nums, target)
        return [minIndex,maxIndex]
    
    def findMinIndex(self, nums, target, index=-1):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index
    
    def findMaxIndex(self, nums, target, index=-1):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index
```
