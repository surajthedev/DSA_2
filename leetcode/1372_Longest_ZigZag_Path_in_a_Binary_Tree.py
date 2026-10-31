# You are given the root of a binary tree.

# A ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

# Return the longest ZigZag path contained in that tree.



# Example 1:


# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
# Example 2:


# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
# Example 3:

# Input: root = [1]
# Output: 0


# Constraints:

# The number of nodes in the tree is in the range [1, 5 * 104].
# 1 <= Node.val <= 100
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
# LeetCode 1372. Longest ZigZag Path in a Binary Tree

### 1. Brute Force (DFS)

python

```python
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, direction, length):
            nonlocal ans

            if not node:
                return

            ans = max(ans, length)

            if direction == 0:
                dfs(node.left, 1, length + 1)
                dfs(node.right, 0, 1)
            else:
                dfs(node.right, 0, length + 1)
                dfs(node.left, 1, 1)

        dfs(root, 0, 0)
        dfs(root, 1, 0)

        return ans
```

### 2. Optimal (Tree DP)

python

```python
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return (-1, -1)

            left = dfs(node.left)
            right = dfs(node.right)

            go_left = left[1] + 1
            go_right = right[0] + 1

            ans = max(ans, go_left, go_right)

            return (go_left, go_right)

        dfs(root)
        return ans
```

### Complexity

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n²) worst case | O(n) |
| Optimal | O(n) | O(h) |

- `n` = number of nodes
- `h` = height of tree

Optimal: O(n)
