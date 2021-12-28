# 547. Number of Provinces

## Medium

***

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `ith` city and the `jth` city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return _the total number of **provinces**_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)

```
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg)

```
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```

&#x20;

**Constraints:**

* `1 <= n <= 200`
* `n == isConnected.length`
* `n == isConnected[i].length`
* `isConnected[i][j]` is `1` or `0`.
* `isConnected[i][i] == 1`
* `isConnected[i][j] == isConnected[j][i] <--- Remember this line while solving`

```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False]*len(isConnected)
        result = []
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] == 1 and not visited[col]:
                    result.append(self.findConnectedNodes(visited, isConnected, col))
        return len(result)
    # Simply Traversing Adjency Matrix
    def findConnectedNodes(self, visited, isConnected, node, connectedNodeList=[]):
        visited[node] = True
        for col in range(len(isConnected[0])):
            if isConnected[node][col] == 1 and not visited[col]:
                connectedNodeList.append(self.findConnectedNodes(visited, isConnected, col))
        return connectedNodeList
```
