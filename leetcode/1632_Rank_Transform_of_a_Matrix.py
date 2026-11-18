# Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

# The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:

# The rank is an integer starting from 1.
# If two elements p and q are in the same row or column, then:
# If p < q then rank(p) < rank(q)
# If p == q then rank(p) == rank(q)
# If p > q then rank(p) > rank(q)
# The rank should be as small as possible.
# The test cases are generated so that answer is unique under the given rules.



# Example 1:


# Input: matrix = [[1,2],[3,4]]
# Output: [[1,2],[2,3]]
# Explanation:
# The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
# The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
# The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
# The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.
# Example 2:


# Input: matrix = [[7,7],[7,7]]
# Output: [[1,1],[1,1]]
# Example 3:


# Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
# Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 500
# -109 <= matrix[row][col] <= 109
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
# ### 1. Brute Force Approach (Sorting + Rank Calculation)

python

```python
from typing import List

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        elements = []

        for i in range(m):
            for j in range(n):
                elements.append((matrix[i][j], i, j))

        elements.sort()

        ans = [[0] * n for _ in range(m)]

        for k in range(m * n):
            val, r, c = elements[k]
            rank = 1

            for i in range(m):
                if matrix[i][c] < val:
                    rank = max(rank, ans[i][c] + 1)

            for j in range(n):
                if matrix[r][j] < val:
                    rank = max(rank, ans[r][j] + 1)

            ans[r][c] = rank

        return ans
```

### 2. Optimal Approach (Sorting + DSU + Grouping)

python

```python
from typing import List
from collections import defaultdict

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        parent = list(range(m + n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        values = defaultdict(list)

        for i in range(m):
            for j in range(n):
                values[matrix[i][j]].append((i, j))

        row_rank = [0] * m
        col_rank = [0] * n

        ans = [[0] * n for _ in range(m)]

        for val in sorted(values):
            parent = list(range(m + n))
            groups = defaultdict(list)

            for r, c in values[val]:
                union(r, m + c)

            for r, c in values[val]:
                root = find(r)
                groups[root].append((r, c))

            for group in groups.values():
                rank = max(
                    max(row_rank[r], col_rank[c]) + 1
                    for r, c in group
                )

                for r, c in group:
                    ans[r][c] = rank

            for r, c in values[val]:
                row_rank[r] = ans[r][c]
                col_rank[c] = ans[r][c]

        return ans
```

### Complexity

| Approach | Time Complexity | Space Complexity |
| --- | --- | --- |
| Brute Force | O((mn)²) | O(mn) |
| Optimal DSU | O(mn log(mn)) | O(mn) |
