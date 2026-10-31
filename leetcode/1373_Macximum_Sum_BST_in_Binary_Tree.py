# Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Example 1:



# Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# Output: 20
# Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
# Example 2:



# Input: root = [4,3,null,1,2]
# Output: 2
# Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
# Example 3:

# Input: root = [-4,-2,-5]
# Output: 0
# Explanation: All values are negatives. Return an empty BST.


# Constraints:

# The number of nodes in the tree is in the range [1, 4 * 104].
# -4 * 104 <= Node.val <= 4 * 104
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
# LeetCode 1373. Maximum Sum BST in Binary Tree

### 1. Brute Force

python

```python
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def is_bst(node, low, high):
            if not node:
                return True, 0

            if not (low < node.val < high):
                return False, 0

            left_valid, left_sum = is_bst(node.left, low, node.val)
            right_valid, right_sum = is_bst(node.right, node.val, high)

            if not left_valid or not right_valid:
                return False, 0

            return True, left_sum + right_sum + node.val

        def dfs(node):
            nonlocal ans

            if not node:
                return

            valid, total = is_bst(node, float('-inf'), float('inf'))

            if valid:
                ans = max(ans, total)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans
```

### 2. Optimal (Postorder DFS + Tree DP)

python

```python
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return float('inf'), float('-inf'), 0

            lmin, lmax, lsum = dfs(node.left)
            rmin, rmax, rsum = dfs(node.right)

            if lmax < node.val < rmin:
                total = lsum + rsum + node.val
                ans = max(ans, total)

                return (
                    min(lmin, node.val),
                    max(rmax, node.val),
                    total
                )

            return float('-inf'), float('inf'), 0

        dfs(root)
        return ans
```

### Complexity

| Approach | Time | Space |
| --- | --- | --- |
| Brute Force | O(n²) | O(h) |
| Optimal | O(n) | O(h) |

- `n` = number of nodes
- `h` = height of tree

Optimal: O(n)
