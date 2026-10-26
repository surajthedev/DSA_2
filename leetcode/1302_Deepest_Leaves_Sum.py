# Given the root of a binary tree, return the sum of values of its deepest leaves.


# Example 1:


# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# Example 2:

# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19


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
#
#
#
#
# ### 1. Brute Force (DFS — Two Passes)

python

```
class Solution:
    def deepestLeavesSum(self, root):
        def getDepth(node):
            if not node:
                return 0
            return 1 + max(getDepth(node.left), getDepth(node.right))

        max_depth = getDepth(root)

        def getSum(node, depth):
            if not node:
                return 0
            if depth == max_depth:
                return node.val
            return getSum(node.left, depth + 1) + getSum(node.right, depth + 1)

        return getSum(root, 1)
```

### 2. Optimal (BFS — Level Order Traversal)

python

```
from collections import deque

class Solution:
    def deepestLeavesSum(self, root):
        queue = deque([root])
        total = 0

        while queue:
            total = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                total += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return total
```
