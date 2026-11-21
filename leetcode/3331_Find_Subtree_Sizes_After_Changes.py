# You are given a tree rooted at node 0 that consists of n nodes numbered from 0 to n - 1. The tree is represented by an array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

# You are also given a string s of length n, where s[i] is the character assigned to node i.

# We make the following changes on the tree one time simultaneously for all nodes x from 1 to n - 1:

# Find the closest node y to node x such that y is an ancestor of x, and s[x] == s[y].
# If node y does not exist, do nothing.
# Otherwise, remove the edge between x and its current parent and make node y the new parent of x by adding an edge between them.
# Return an array answer of size n where answer[i] is the size of the subtree rooted at node i in the final tree.



# Example 1:

# Input: parent = [-1,0,0,1,1,1], s = "abaabc"

# Output: [6,3,1,1,1,1]

# Explanation:


# The parent of node 3 will change from node 1 to node 0.

# Example 2:

# Input: parent = [-1,0,4,0,1], s = "abbba"

# Output: [5,2,1,1,1]

# Explanation:


# The following changes will happen at the same time:

# The parent of node 4 will change from node 1 to node 0.
# The parent of node 2 will change from node 4 to node 1.


# Constraints:

# n == parent.length == s.length
# 1 <= n <= 105
# 0 <= parent[i] <= n - 1 for all i >= 1.
# parent[0] == -1
# parent represents a valid tree.
# s consists only of lowercase English letters.
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

Time: O(N²) — Space: O(N)python

```python
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        new_parent = parent[:]

        for x in range(1, n):
            y = parent[x]

            while y != -1:
                if s[x] == s[y]:
                    new_parent[x] = y
                    break
                y = parent[y]

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[new_parent[i]].append(i)

        ans = [0] * n

        def dfs(node):
            ans[node] = 1
            for child in children[node]:
                ans[node] += dfs(child)
            return ans[node]

        dfs(0)
        return ans
```

### 2. Optimal Approach

Time: O(N) — Space: O(N)python

```python
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}

        def dfs(node):
            ch = s[node]
            old = last.get(ch, -1)

            if old != -1:
                new_parent[node] = old

            last[ch] = node

            for child in children[node]:
                dfs(child)

            if old == -1:
                last.pop(ch, None)
            else:
                last[ch] = old

        dfs(0)

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [1] * n

        def calculate(node):
            for child in new_children[node]:
                calculate(child)
                ans[node] += ans[child]

        calculate(0)

        return ans
```
