# 90. Subsets II

## Medium

***

Given an integer array `nums` that may contain duplicates, return _all possible subsets (the power set)_.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

&#x20;

**Example 1:**

```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**Example 2:**

```
Input: nums = [0]
Output: [[],[0]]
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 10`
* `-10 <= nums[i] <= 1`

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def recursion(nums, start, path, result):
            result.append(path[:])
            for index in range(start, len(nums)):
                # Eliminate the dup with sort and then the condition: do not put this element inside, if it has same element before && the former dup has not been put into it. 
                if index != start and nums[index] == nums[index-1]:
                    continue
                path.append(nums[index])
                # print(path)
                recursion(nums, index+1, path, result)
                path.pop()
        result = []
        recursion(nums, 0, [], result)
        return result
```
