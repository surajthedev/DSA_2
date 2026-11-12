# You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

# Return the number of good leaf node pairs in the tree.



# Example 1:


# Input: root = [1,2,3,null,4], distance = 3
# Output: 1
# Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
# Example 2:


# Input: root = [1,2,3,4,5,6,7], distance = 3
# Output: 2
# Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
# Example 3:

# Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
# Output: 1
# Explanation: The only good pair is [2,5].


# Constraints:

# The number of nodes in the tree is in the range [1, 210].
# 1 <= Node.val <= 100
# 1 <= distance <= 10
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
# ### 1. Brute Force – O(n² × h)

python

```python
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        leaves = []

        def findLeaves(node, path):
            if not node:
                return

            if not node.left and not node.right:
                leaves.append(path)
                return

            findLeaves(node.left, path + [node])
            findLeaves(node.right, path + [node])

        findLeaves(root, [])

        ans = 0

        for i in range(len(leaves)):
            for j in range(i + 1, len(leaves)):
                p1 = leaves[i]
                p2 = leaves[j]

                k = 0
                while k < min(len(p1), len(p2)) and p1[k] == p2[k]:
                    k += 1

                dist = len(p1) + len(p2) - 2 * k + 2

                if dist <= distance:
                    ans += 1

        return ans
```

### 2. Optimal – DFS + Tree DP

Time Complexity: O(n × distance²) Space Complexity: O(n × distance)

python

```python
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return []

            if not node.left and not node.right:
                return [1]

            left = dfs(node.left)
            right = dfs(node.right)

            for l in left:
                for r in right:
                    if l + r <= distance:
                        ans += 1

            res = []

            for d in left + right:
                if d + 1 < distance:
                    res.append(d + 1)

            return res

        dfs(root)
        return ans
```
