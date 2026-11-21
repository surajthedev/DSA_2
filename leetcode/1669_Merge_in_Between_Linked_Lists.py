# You are given two linked lists: list1 and list2 of sizes n and m respectively.

# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

# The blue edges and nodes in the following figure indicate the result:


# Build the result list and return its head.



# Example 1:


# Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [10,1,13,1000000,1000001,1000002,5]
# Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
# Example 2:


# Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
# Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
# Explanation: The blue edges and nodes in the above figure indicate the result.


# Constraints:

# 3 <= list1.length <= 104
# 1 <= a <= b < list1.length - 1
# 1 <= list2.length <= 104
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# ### 1. Brute Force Approach

python

```python
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = list1

        prev = dummy

        for _ in range(a):
            prev = prev.next

        after = prev
        for _ in range(b - a + 2):
            after = after.next

        prev.next = list2

        tail = list2
        while tail.next:
            tail = tail.next

        tail.next = after

        return dummy.next
```

### 2. Optimal Approach

Time: O(N + M) — Space: O(1)python

```python
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = list1

        for _ in range(a - 1):
            prev = prev.next

        after = prev
        for _ in range(b - a + 2):
            after = after.next

        tail = list2

        while tail.next:
            tail = tail.next

        prev.next = list2
        tail.next = after

        return list1
```
