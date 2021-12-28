# partition-to-equal-k-subset

Given an integer array `nums` and an integer `k`, return `true` if it is possible to divide this array into `k` non-empty subsets whose sums are all equal.

&#x20;

**Example 1:**

```
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
```

**Example 2:**

```
Input: nums = [1,2,3,4], k = 3
Output: false
```

&#x20;

**Constraints:**

* `1 <= k <= nums.length <= 16`
* `1 <= nums[i] <= 104`
* The frequency of each element is in the range `[1, 4]`.

```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total%k:
            return False
        target=total//k
        length=len(nums)
        used=[False]*length

        def Helper(i,k,currentSum):
            if k==0:
                return True
            if currentSum==target:
                return Helper(0,k-1,0)
            for j in range(i,length):
                newCurrentSum=currentSum+nums[j]
                if used[j] or newCurrentSum>target:
                    continue
                used[j]=True
                if Helper(j,k,newCurrentSum):
                    return True
                used[j]=False
            return False
        return Helper(0 , k, 0)
```
