# You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

# The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

# In one day, we are allowed to change any single land cell (1) into a water cell (0).

# Return the minimum number of days to disconnect the grid.



# Example 1:


# Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

# Output: 2
# Explanation: We need at least 2 days to get a disconnected grid.
# Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
# Example 2:


# Input: grid = [[1,1]]
# Output: 2
# Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 30
# grid[i][j] is either 0 or 1.
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
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def countIslands():
            visited = set()
            islands = 0

            def dfs(r, c):
                visited.add((r, c))

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < m and 0 <= nc < n
                        and grid[nr][nc] == 1
                        and (nr, nc) not in visited):
                        dfs(nr, nc)

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        islands += 1
                        dfs(i, j)

            return islands

        if countIslands() != 1:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0

                    if countIslands() != 1:
                        grid[i][j] = 1
                        return 1

                    grid[i][j] = 1

        return 2
```

Time Complexity: O((m × n)²) Space Complexity: O(m × n)

### 2. Optimal Approach (Tarjan's Algorithm – Articulation Point)
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        land = sum(row.count(1) for row in grid)

        if land <= 1:
            return land

        def countIslands():
            visited = set()
            islands = 0

            def dfs(r, c):
                visited.add((r, c))

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < m and 0 <= nc < n
                        and grid[nr][nc] == 1
                        and (nr, nc) not in visited):
                        dfs(nr, nc)

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        islands += 1
                        dfs(i, j)

            return islands

        if countIslands() != 1:
            return 0

        disc = [[-1] * n for _ in range(m)]
        low = [[-1] * n for _ in range(m)]
        timer = 0
        has_articulation = False

        def dfs(r, c, pr, pc):
            nonlocal timer, has_articulation

            disc[r][c] = low[r][c] = timer
            timer += 1
            children = 0

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if grid[nr][nc] == 0 or (nr, nc) == (pr, pc):
                    continue

                if disc[nr][nc] == -1:
                    children += 1
                    dfs(nr, nc, r, c)

                    low[r][c] = min(low[r][c], low[nr][nc])

                    if pr != -1 and low[nr][nc] >= disc[r][c]:
                        has_articulation = True

                else:
                    low[r][c] = min(low[r][c], disc[nr][nc])

            if pr == -1 and children > 1:
                has_articulation = True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, -1, -1)
                    break
            else:
                continue
            break

        return 1 if has_articulation else 2
