# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.



# Example 1:


# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:


# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1


# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
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
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        visited = set()
        ans = [float('inf')]
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        def dfs(r, c, length):
            if length >= ans[0]:
                return

            if r == n - 1 and c == n - 1:
                ans[0] = length
                return

            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and 0 <= nc < n
                        and grid[nr][nc] == 0
                        and (nr, nc) not in visited):
                    dfs(nr, nc, length + 1)

            visited.remove((r, c))

        dfs(0, 0, 1)
        return ans[0] if ans[0] != float('inf') else -1
```

### Optimal (BFS)

python
```
from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        queue = deque([(0, 0, 1)])
        grid[0][0] = 1

        while queue:
            r, c, length = queue.popleft()

            if r == n - 1 and c == n - 1:
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, length + 1))

        return -1
```
