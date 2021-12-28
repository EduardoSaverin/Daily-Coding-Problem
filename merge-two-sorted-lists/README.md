# 21. Merge Two Sorted Lists

## Easy

***

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return _the head of the merged linked list_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/merge\_ex1.jpg)

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:**

```
Input: list1 = [], list2 = []
Output: []
```

**Example 3:**

```
Input: list1 = [], list2 = [0]
Output: [0]
```

&#x20;

**Constraints:**

* The number of nodes in both lists is in the range `[0, 50]`.
* `-100 <= Node.val <= 100`
* Both `list1` and `list2` are sorted in **non-decreasing** order.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        elif not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1
        head = None
        pointer = None
        while list1 and list2:
            temp = None
            if list1.val < list2.val:
                temp = list1
                list1 = list1.next
            else:
                temp = list2
                list2 = list2.next
            if temp is not None:
                if head is None:
                    head = pointer = temp
                    temp.next = None
                else:
                    pointer.next = temp
                    pointer = temp
        if list1 is not None:
            pointer.next = list1
        elif list2 is not None:
            pointer.next = list2
        return headputh
```
