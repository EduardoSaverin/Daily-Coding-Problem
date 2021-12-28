# 347. Top K Frequent Elements

## Medium

***

Given an integer array `nums` and an integer `k`, return _the_ `k` _most frequent elements_. You may return the answer in **any order**.

&#x20;

**Example 1:**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

&#x20;

**Constraints:**

* `1 <= nums.length <= 105`
* `k` is in the range `[1, the number of unique elements in the array]`.
* It is **guaranteed** that the answer is **unique**.

&#x20;

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num: nums) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num , 1);
            }
        }
        class Pair {
            int num;
            int count;
            Pair(int num, int count) {
                this.num = num;
                this.count = count;
            }
        }
        Comparator<Pair> comp = new Comparator<Pair>() {
            public int compare(Pair p1, Pair p2) {
                if (p1.count == p2.count) {
                    return p1.num - p2.num;
                }
                return p1.count - p2.count;
            }
        };
        PriorityQueue<Pair> queue = new PriorityQueue<Pair>(k, comp);
        for (int num : nums) {
            if (!map.containsKey(num)) {
                continue;
            }
            Pair p = new Pair(num, map.get(num));
            if (queue.size() < k) {
                queue.offer(p);
            } else {
                Pair top = queue.peek();
                if (top.count < p.count) {
                    queue.poll();
                    queue.offer(p);
                }
            }
            map.remove(num);
        }
        int[] result = new int[k];
        int index = 0;
        for (Pair p : queue) {
                result[index++] = (p.num);
            }
            return result;
    }
}
```
