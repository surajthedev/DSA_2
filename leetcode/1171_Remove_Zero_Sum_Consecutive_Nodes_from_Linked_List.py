# Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

# After doing so, return the head of the final linked list.  You may return any such answer.



# (Note that in the examples below, all sequences are serializations of ListNode objects.)

# Example 1:

# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.
# Example 2:

# Input: head = [1,2,3,-3,4]
# Output: [1,2,4]
# Example 3:

# Input: head = [1,2,3,-3,-2]
# Output: [1]


# Constraints:

# The given linked list will contain between 1 and 1000 nodes.
# Each node in the linked list has -1000 <= node.val <= 1000.
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
# ### 1. Brute Force — O(n²)

python
```
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        while True:
            prefix = 0
            seen = {0: dummy}
            node = dummy.next
            removed = False

            while node:
                prefix += node.val

                if prefix in seen:
                    prev = seen[prefix]
                    prev.next = node.next
                    removed = True
                    break

                seen[prefix] = node
                node = node.next

            if not removed:
                return dummy.next
```

### 2. Optimal Solution — O(n) Time, O(n) Space

python
```
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prefix = 0
        last_seen = {}
        node = dummy

        while node:
            prefix += node.val
            last_seen[prefix] = node
            node = node.next

        prefix = 0
        node = dummy

        while node:
            prefix += node.val
            node.next = last_seen[prefix].next
            node = node.next

        return dummy.next
```
