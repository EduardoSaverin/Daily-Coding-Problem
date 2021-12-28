# 416. Partition Equal Subset Sum

## Medium

***

Given a **non-empty** array `nums` containing **only positive integers**, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

&#x20;

**Example 1:**

```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

**Example 2:**

```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 200`
* `1 <= nums[i] <= 100`

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2
        if total%2 == 1 or len(nums) == 1:
            return False
        d = {}
        def recursion(target, index, d):
            if target < 0 or index == len(nums):
                return False
            elif target == 0:
                return True
            elif (index, target) in d:
                return d[(index, target)]
            value = recursion(target - nums[index], index+1, d) or recursion(target, index+1, d)
            d[(index, target)] = value
            return value
        return recursion(target, 0, d)
```
