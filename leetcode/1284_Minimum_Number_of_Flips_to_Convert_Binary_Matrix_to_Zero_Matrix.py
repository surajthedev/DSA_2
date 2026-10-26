# Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbors of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighbors if they share one edge.

# Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.

# A binary matrix is a matrix with all cells equal to 0 or 1 only.

# A zero matrix is a matrix with all cells equal to 0.



# Example 1:


# Input: mat = [[0,0],[0,1]]
# Output: 3
# Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.
# Example 2:

# Input: mat = [[0]]
# Output: 0
# Explanation: Given matrix is a zero matrix. We do not need to change it.
# Example 3:

# Input: mat = [[1,0,0],[1,0,0]]
# Output: -1
# Explanation: Given matrix cannot be a zero matrix.


# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 3
# mat[i][j] is either 0 or 1.
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
# Brute force:

from collections import deque

class Solution:
    def minFlips(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        start = tuple(mat[i][j] for i in range(m) for j in range(n))
        target = (0,) * (m * n)

        if start == target:
            return 0

        moves = []
        directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(m):
            for c in range(n):
                mask = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        mask |= 1 << (nr * n + nc)
                moves.append(mask)

        initial = sum(bit << i for i, bit in enumerate(start))
        target = 0
        queue = deque([(initial, 0)])
        visited = {initial}

        while queue:
            state, steps = queue.popleft()

            for mask in moves:
                nxt = state ^ mask

                if nxt == target:
                    return steps + 1

                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))

        return -1
















# Optimal:
### Brute Force (BFS)

python

```

from collections import deque

class Solution:
    def minFlips(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        start = tuple(mat[i][j] for i in range(m) for j in range(n))
        target = (0,) * (m * n)

        if start == target:
            return 0

        moves = []
        directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(m):
            for c in range(n):
                mask = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        mask |= 1 << (nr * n + nc)
                moves.append(mask)

        initial = sum(bit << i for i, bit in enumerate(start))
        target = 0
        queue = deque([(initial, 0)])
        visited = {initial}

        while queue:
            state, steps = queue.popleft()

            for mask in moves:
                nxt = state ^ mask

                if nxt == target:
                    return steps + 1

                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))

        return -1
```

### Optimal (Bitmask BFS)

python

```

from collections import deque

class Solution:
    def minFlips(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        start = 0

        for r in range(m):
            for c in range(n):
                if mat[r][c]:
                    start |= 1 << (r * n + c)

        if start == 0:
            return 0

        moves = []
        directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(m):
            for c in range(n):
                mask = 0

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        mask ^= 1 << (nr * n + nc)

                moves.append(mask)

        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            state, steps = queue.popleft()

            for mask in moves:
                nxt = state ^ mask

                if nxt == 0:
                    return steps + 1

                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))

        return -1
```
