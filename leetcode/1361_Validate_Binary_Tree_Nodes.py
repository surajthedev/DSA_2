# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

# Note that the nodes have no values and that we only use the node numbers in this problem.



# Example 1:


# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true
# Example 2:


# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# Output: false
# Example 3:


# Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
# Output: false


# Constraints:

# n == leftChild.length == rightChild.length
# 1 <= n <= 104
# -1 <= leftChild[i], rightChild[i] <= n - 1
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
# ### Brute Force (BFS)

python

```
from collections import deque

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        indegree = [0] * n

        for i in range(n):
            for child in (leftChild[i], rightChild[i]):
                if child != -1:
                    indegree[child] += 1

        roots = [i for i in range(n) if indegree[i] == 0]

        if len(roots) != 1:
            return False

        q = deque([roots[0]])
        visited = set()

        while q:
            node = q.popleft()

            if node in visited:
                return False

            visited.add(node)

            for child in (leftChild[node], rightChild[node]):
                if child != -1:
                    q.append(child)

        return len(visited) == n
```

Time Complexity: $O(n)$

Space Complexity: $O(n)$

### Optimal Solution (DFS)

python

```
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        indegree = [0] * n

        for i in range(n):
            for child in (leftChild[i], rightChild[i]):
                if child != -1:
                    indegree[child] += 1

                    if indegree[child] > 1:
                        return False

        roots = [i for i in range(n) if indegree[i] == 0]

        if len(roots) != 1:
            return False

        visited = set()

        def dfs(node):
            if node == -1:
                return True

            if node in visited:
                return False

            visited.add(node)

            return dfs(leftChild[node]) and dfs(rightChild[node])

        return dfs(roots[0]) and len(visited) == n
```

Time Complexity: $O(n)$

Space Complexity: $O(n)$
