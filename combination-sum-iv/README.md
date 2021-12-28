# 377. Combination Sum IV

## Medium

***

Given an array of **distinct** integers `nums` and a target integer `target`, return _the number of possible combinations that add up to_ `target`.

The test cases are generated so that the answer can fit in a **32-bit** integer.

&#x20;

**Example 1:**

```
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
```

**Example 2:**

```
Input: nums = [9], target = 3
Output: 0
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 200`
* `1 <= nums[i] <= 1000`
* All the elements of `nums` are **unique**.
* `1 <= target <= 1000`

&#x20;

**Follow up:** What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?



Solution

```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort() # For Early Exit
        arr = [0]*(target+1)
        for num in nums:
            if num <= target:
                arr[num] = 1
        for i in range(target+1):
            for num in nums:
                if i-num > 0:
                    arr[i] += arr[i-num]
                else:
                    break
        return arr[-1]
```
