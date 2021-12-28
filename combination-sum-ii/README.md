# 40. Combination Sum II

## Medium

***

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

&#x20;

**Example 1:**

```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

**Example 2:**

```
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
```

&#x20;

**Constraints:**

* `1 <= candidates.length <= 100`
* `1 <= candidates[i] <= 50`
* `1 <= target <= 30`

Solution

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        print(candidates)
        def recursion(candidates, start, path, total, target):
            nonlocal result
            if target == total:
                result.append(path[:])
                return
            for index in range(start, len(candidates)):
                if index > start and candidates[index] == candidates[index-1]:
                    continue
                if total+candidates[index] > target:
                    break
                path.append(candidates[index])
                recursion(candidates,index+1, path, total+candidates[index], target)
                path.pop()
        recursion(candidates,0,[],0, target)
        return result
```
