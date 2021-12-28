# 82. Remove Duplicates from Sorted List II

## Medium

***

Given the `head` of a sorted linked list, _delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list_. Return _the linked list **sorted** as well_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg)

```
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg)

```
Input: head = [1,1,1,2,3]
Output: [2,3]
```

&#x20;

**Constraints:**

* The number of nodes in the list is in the range `[0, 300]`.
* `-100 <= Node.val <= 100`
* The list is guaranteed to be **sorted** in ascending order.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        new = head
        prev = None
        old = None
        if head.next is None:
            return head
        prev = new
        new = new.next
        repeat = False
        newHead = None
        while new:
            if new.val != prev.val:
                if not repeat:
                    if old is None:
                        old = prev
                        if newHead is None:
                            newHead = old
                    else:
                        old.next = prev
                        old = prev
                prev = new
                new = new.next
                repeat = False
            elif new.val == prev.val:
                repeat = True
                prev = new
                new = new.next
        if newHead is None and not repeat:
            return prev
        elif newHead is None:
            return None
        if not repeat:
            old.next = prev
        else:
            old.next = None
        return newHead
```
