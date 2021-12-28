# 55. Jump Game

## Medium

***

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` _if you can reach the last index, or_ `false` _otherwise_.

&#x20;

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 104`
* `0 <= nums[i] <= 105`

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        maxJump = 0
        index = 0
        # If Current Index goes greater than maxJump (totally done till now) so far break the loop
        while index <= maxJump:
            maxJump = max(index + nums[index], maxJump)
            if maxJump >= target:
                return True
            index += 1
        return False
        
            
        
```
