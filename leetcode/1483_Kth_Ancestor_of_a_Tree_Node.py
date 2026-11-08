# You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of ith node. The root of the tree is node 0. Find the kth ancestor of a given node.

# The kth ancestor of a tree node is the kth node in the path from that node to the root node.

# Implement the TreeAncestor class:

# TreeAncestor(int n, int[] parent) Initializes the object with the number of nodes in the tree and the parent array.
# int getKthAncestor(int node, int k) return the kth ancestor of the given node node. If there is no such ancestor, return -1.


# Example 1:


# Input
# ["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
# [[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]
# Output
# [null, 1, 0, -1]

# Explanation
# TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
# treeAncestor.getKthAncestor(3, 1); // returns 1 which is the parent of 3
# treeAncestor.getKthAncestor(5, 2); // returns 0 which is the grandparent of 5
# treeAncestor.getKthAncestor(6, 3); // returns -1 because there is no such ancestor


# Constraints:

# 1 <= k <= n <= 5 * 104
# parent.length == n
# parent[0] == -1
# 0 <= parent[i] < n for all 0 < i < n
# 0 <= node < n
# There will be at most 5 * 104 queries.
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
# ### 1. Brute Force Approach (Parent Traversal)

python

```python
from typing import List

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.parent = parent

    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1:
            node = self.parent[node]
            k -= 1

        return node
```

Time Complexity:

- Constructor: O(1)
- `getKthAncestor`: O(k)

Space Complexity: O(n)

### 2. Optimal Approach (Binary Lifting)

python

```python
from typing import List

class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.LOG = n.bit_length()

        self.up = [[-1] * self.LOG for _ in range(n)]

        for i in range(n):
            self.up[i][0] = parent[i]

        for j in range(1, self.LOG):
            for i in range(n):
                prev = self.up[i][j - 1]

                if prev != -1:
                    self.up[i][j] = self.up[prev][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:

        bit = 0

        while k > 0:
            if k & 1:
                node = self.up[node][bit]

                if node == -1:
                    return -1

            k >>= 1
            bit += 1

        return node
```

Time Complexity:

- Constructor: O(n log n)
- `getKthAncestor`: O(log n)

Space Complexity: O(n log n)
