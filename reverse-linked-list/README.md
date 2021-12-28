# 206. Reverse Linked List

## Easy

***

Given the `head` of a singly linked list, reverse the list, and return _the reversed list_.

&#x20;

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

```
Input: head = [1,2]
Output: [2,1]
```

**Example 3:**

```
Input: head = []
Output: []
```

&#x20;

**Constraints:**

* The number of nodes in the list is the range `[0, 5000]`.
* `-5000 <= Node.val <= 5000`

&#x20;

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        elif head.next is None:
            return head
        tail = None
        def recursion(head):
            nonlocal tail
            if head.next:
                # 5 = (4.next)
                # 4 = (3.next)
                node = recursion(head.next)
                if tail is None:
                    tail = node
                # print(head, head.next, node)
                # 4.next = None
                # 3.next = None
                head.next = None
                if node is None:
                    return head
                # 5.next = 4
                # 4.next = 3
                node.next = head
                # print('Node', node)
                # 4
                # 3 = 4.next
                node = node.next
                # print('Nodes Next', node)
                return node
            else:
                return head
        recursion(head)
        return tail
```
