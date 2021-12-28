# 147. Insertion Sort List

## Medium

***

Given the `head` of a singly linked list, sort the list using **insertion sort**, and return _the sorted list's head_.

The steps of the **insertion sort** algorithm:

1. Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
3. It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

![](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/04/sort1linked-list.jpg)

```
Input: head = [4,2,1,3]
Output: [1,2,3,4]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/04/sort2linked-list.jpg)

```
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

&#x20;

**Constraints:**

* The number of nodes in the list is in the range `[1, 5000]`.
* `-5000 <= Node.val <= 5000`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node = head.next
        head.next = None
        while node:
            next_node = node.next
            ptr = dummy
            # note that we are creating reverse list here just like insertion order
            while ptr.next and ptr.next.val > node.val:
                ptr = ptr.next
            node.next = ptr.next
            ptr.next = node
            node = next_node
        node  = dummy.next
        head = None
        # Simple Reversing
        while node:
            next_node = node.next
            node.next = head
            head = node
            node = next_node
        return head
```
