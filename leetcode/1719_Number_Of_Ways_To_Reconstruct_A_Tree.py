# You are given an array pairs, where pairs[i] = [xi, yi], and:

# There are no duplicates.
# xi < yi
# Let ways be the number of rooted trees that satisfy the following conditions:

# The tree consists of nodes whose values appeared in pairs.
# A pair [xi, yi] exists in pairs if and only if xi is an ancestor of yi or yi is an ancestor of xi.
# Note: the tree does not have to be a binary tree.
# Two ways are considered to be different if there is at least one node that has different parents in both ways.

# Return:

# 0 if ways == 0
# 1 if ways == 1
# 2 if ways > 1
# A rooted tree is a tree that has a single root node, and all edges are oriented to be outgoing from the root.

# An ancestor of a node is any node on the path from the root to that node (excluding the node itself). The root has no ancestors.



# Example 1:


# Input: pairs = [[1,2],[2,3]]
# Output: 1
# Explanation: There is exactly one valid rooted tree, which is shown in the above figure.
# Example 2:


# Input: pairs = [[1,2],[2,3],[1,3]]
# Output: 2
# Explanation: There are multiple valid rooted trees. Three of them are shown in the above figures.
# Example 3:

# Input: pairs = [[1,2],[2,3],[2,4],[1,5]]
# Output: 0
# Explanation: There are no valid rooted trees.


# Constraints:

# 1 <= pairs.length <= 105
# 1 <= xi < yi <= 500
# The elements in pairs are unique.
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
#
# ### 1. Brute Force Approach

python

```python
from typing import List
from itertools import permutations

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        nodes = set()
        for x, y in pairs:
            nodes.add(x)
            nodes.add(y)

        nodes = list(nodes)
        n = len(nodes)

        adj = {x: set() for x in nodes}

        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)

        ans = set()

        for root in nodes:
            def build(parent, visited):
                if len(visited) == n:
                    ans.add(tuple(sorted(parent.items())))
                    return

                for node in nodes:
                    if node not in visited:
                        continue

                for node in nodes:
                    if node in visited:
                        continue

                    possible = [
                        p for p in visited
                        if node in adj[p]
                    ]

                    for p in possible:
                        parent[node] = p
                        visited.add(node)
                        build(parent, visited)
                        visited.remove(node)
                        del parent[node]

            build({}, {root})

            if len(ans) > 1:
                return 2

        return 1 if ans else 0
```

### 2. Optimal Approach (Graph + Greedy)

python

```python
from typing import List

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        adj = {}

        for x, y in pairs:
            adj.setdefault(x, set()).add(y)
            adj.setdefault(y, set()).add(x)

        nodes = list(adj.keys())
        n = len(nodes)

        root = None

        for node in nodes:
            if len(adj[node]) == n - 1:
                root = node
                break

        if root is None:
            return 0

        ans = 1

        for node in nodes:
            if node == root:
                continue

            parent = None
            parent_degree = float('inf')

            for neighbor in adj[node]:
                if len(adj[neighbor]) >= len(adj[node]) and len(adj[neighbor]) < parent_degree:
                    parent = neighbor
                    parent_degree = len(adj[neighbor])

            if parent is None:
                return 0

            for neighbor in adj[node]:
                if neighbor != parent and neighbor not in adj[parent]:
                    return 0

            if len(adj[parent]) == len(adj[node]):
                ans = 2

        return ans
```

Time Complexity: $O(n^2)$ worst case

Space Complexity: $O(n^2)$ for the adjacency sets.
