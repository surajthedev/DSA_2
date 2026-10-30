# Given a binary tree root and a linked list with head as the first node.

# Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

# In this context downward path means a path that starts at some node and goes downwards.



# Example 1:



# Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# Explanation: Nodes in blue form a subpath in the binary Tree.
# Example 2:



# Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# Example 3:

# Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: false
# Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.


# Constraints:

# The number of nodes in the tree will be in the range [1, 2500].
# The number of nodes in the list will be in the range [1, 100].
# 1 <= Node.val <= 100 for each node in the linked list and binary tree.
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
# ### Brute Force Solution (DFS)

python

```
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def check(node, curr):
            if curr is None:
                return True

            if node is None or node.val != curr.val:
                return False

            return check(node.left, curr.next) or check(node.right, curr.next)

        if root is None:
            return False

        return (
            check(root, head)
            or self.isSubPath(head, root.left)
            or self.isSubPath(head, root.right)
        )
```

Time Complexity: $O(N \times M)$

Space Complexity: $O(H + M)$

### Optimal Solution (DFS + KMP)

python

```
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        pattern = []

        while head:
            pattern.append(head.val)
            head = head.next

        m = len(pattern)

        lps = [0] * m
        j = 0

        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]

            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j

        def dfs(node, j):
            if node is None:
                return False

            while j > 0 and node.val != pattern[j]:
                j = lps[j - 1]

            if node.val == pattern[j]:
                j += 1

            if j == m:
                return True

            return dfs(node.left, j) or dfs(node.right, j)

        return dfs(root, 0)
```

Time Complexity: $O(N + M)$

Space Complexity: $O(M + H)$

- `N` = Number of tree nodes
- `M` = Number of linked list nodes
- `H` = Height of binary tree
