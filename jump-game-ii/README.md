# 45. Jump Game II

## Medium

***

Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

&#x20;

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: nums = [2,3,0,1,4]
Output: 2
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 104`
* `0 <= nums[i] <= 1000`

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        # Trying Simple Iterative Solution
        target = len(nums)-1
        start,end = 0,0
        maxJump = 0
        count = 0
        while end < target:
            count += 1
            for index in range(start, end+1):
                maxJump = max(maxJump, index + nums[index])
            if maxJump >= target:
                return count
            start = end+1
            end = maxJump
        return count
            
```
