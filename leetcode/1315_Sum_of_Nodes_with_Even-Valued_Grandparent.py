# Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

# A grandparent of a node is the parent of its parent if it exists.



# Example 1:


# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
# Example 2:


# Input: root = [1]
# Output: 0


# Constraints:

# The number of nodes in the tree is in the range [1, 104].
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
# ### Brute Force (DFS)

python

```
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent, grandparent):
            if not node:
                return 0

            total = 0
            if grandparent and grandparent.val % 2 == 0:
                total += node.val

            total += dfs(node.left, node, parent)
            total += dfs(node.right, node, parent)

            return total

        return dfs(root, None, None)
```

### Optimal (DFS)

python

```
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            total = 0

            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        total += node.left.left.val
                    if node.left.right:
                        total += node.left.right.val

                if node.right:
                    if node.right.left:
                        total += node.right.left.val
                    if node.right.right:
                        total += node.right.right.val

            return total + dfs(node.left) + dfs(node.right)

        return dfs(root)
```
