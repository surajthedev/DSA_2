# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).



# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]


# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 105
# 0 <= Node.val <= 100
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
# ### 1. Brute Force Approach (Array)

python

```python
from typing import Optional

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        n = len(nodes)

        nodes[k - 1].val, nodes[n - k].val = (
            nodes[n - k].val,
            nodes[k - 1].val
        )

        return head
```

### 2. Optimal Approach (Two Pointers)

python

```python
from typing import Optional

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head

        for _ in range(k - 1):
            first = first.next

        slow = head
        fast = first

        while fast.next:
            slow = slow.next
            fast = fast.next

        first.val, slow.val = slow.val, first.val

        return head
```

Time Complexity: $O(n)$

Space Complexity:

- Brute Force: $O(n)$
- Optimal: $O(1)$
