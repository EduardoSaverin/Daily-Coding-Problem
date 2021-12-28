# 1200. Minimum Absolute Difference

## Easy

***

Given an array of **distinct** integers `arr`, find all pairs of elements with the minimum absolute difference of any two elements.&#x20;

Return a list of pairs in ascending order(with respect to pairs), each pair `[a, b]` follows

* `a, b` are from `arr`
* `a < b`
* `b - a` equals to the minimum absolute difference of any two elements in `arr`

&#x20;

**Example 1:**

```
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
```

**Example 2:**

```
Input: arr = [1,3,6,10,15]
Output: [[1,3]]
```

**Example 3:**

```
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
```

&#x20;

**Constraints:**

* `2 <= arr.length <= 10^5`
* `-10^6 <= arr[i] <= 10^6`

```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = 10000000
        result = []
        for index in range(1, len(arr)):
            if abs(arr[index] - arr[index-1]) < diff:
                diff = abs(arr[index] - arr[index-1])
        
        for index in range(1, len(arr)):
            if abs(arr[index] - arr[index-1]) == diff:
                result.append([arr[index-1], arr[index]])
        return result
```
