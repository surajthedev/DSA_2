# Given an m x n binary grid grid where:

# grid[i][j] == 0 represents an empty cell, and
# grid[i][j] == 1 represents a mirror.
# A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). It can move only right or down. If the robot attempts to move into a mirror cell, it is reflected before entering that cell:

# If it tries to move right into a mirror, it is turned down and moved into the cell directly below the mirror.
# If it tries to move down into a mirror, it is turned right and moved into the cell directly to the right of the mirror.
# If this reflection would cause the robot to move outside the grid boundaries, the path is considered invalid and should not be counted.

# Return the number of unique valid paths from (0, 0) to (m - 1, n - 1).

# Since the answer may be very large, return it modulo 109 + 7.

# Note: If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.



# Example 1:

# Input: grid = [[0,1,0],[0,0,1],[1,0,0]]

# Output: 5

# Explanation:

# Number	Full Path
# 1	(0, 0) → (0, 1) [M] → (1, 1) → (1, 2) [M] → (2, 2)
# 2	(0, 0) → (0, 1) [M] → (1, 1) → (2, 1) → (2, 2)
# 3	(0, 0) → (1, 0) → (1, 1) → (1, 2) [M] → (2, 2)
# 4	(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)
# 5	(0, 0) → (1, 0) → (2, 0) [M] → (2, 1) → (2, 2)
# [M] indicates the robot attempted to enter a mirror cell and instead reflected.

# Example 2:

# Input: grid = [[0,0],[0,0]]

# Output: 2

# Explanation:

# Number	Full Path
# 1	(0, 0) → (0, 1) → (1, 1)
# 2	(0, 0) → (1, 0) → (1, 1)
# Example 3:

# Input: grid = [[0,1,1],[1,1,0]]

# Output: 1

# Explanation:

# Number	Full Path
# 1	(0, 0) → (0, 1) [M] → (1, 1) [M] → (1, 2)
# (0, 0) → (1, 0) [M] → (1, 1) [M] → (2, 1) goes out of bounds, so it is invalid.


# Constraints:

# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 500
# grid[i][j] is either 0 or 1.
# grid[0][0] == grid[m - 1][n - 1] == 0
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
# **Brute Force (DFS)**

```python
import sys
sys.setrecursionlimit(10**6)

class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            # (i, j) is an empty cell
            if i == m - 1 and j == n - 1:
                return 1
            total = 0

            # try moving right
            r, c, d = i, j + 1, 0  # d: 0 = right, 1 = down
            while True:
                if r >= m or c >= n:
                    break
                if grid[r][c] == 0:
                    total += dfs(r, c)
                    break
                # mirror
                if d == 0:
                    r, d = r + 1, 1
                else:
                    c, d = c + 1, 0

            # try moving down
            r, c, d = i + 1, j, 1
            while True:
                if r >= m or c >= n:
                    break
                if grid[r][c] == 0:
                    total += dfs(r, c)
                    break
                if d == 0:
                    r, d = r + 1, 1
                else:
                    c, d = c + 1, 0

            return total % MOD

        return dfs(0, 0)
```










# **Optimal (DP, O(m·n) time and space)**

```python
class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # R[i][j] = ways arriving at (i, j) while moving right
        # D[i][j] = ways arriving at (i, j) while moving down
        R = [[0] * n for _ in range(m)]
        D = [[0] * n for _ in range(m)]
        R[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                # coming from left cell (i, j-1)
                if j > 0:
                    if grid[i][j - 1] == 0:
                        R[i][j] = (R[i][j - 1] + D[i][j - 1]) % MOD
                    else:
                        R[i][j] = D[i][j - 1]  # entered mirror moving down -> turn right

                # coming from up cell (i-1, j)
                if i > 0:
                    if grid[i - 1][j] == 0:
                        D[i][j] = (R[i - 1][j] + D[i - 1][j]) % MOD
                    else:
                        D[i][j] = R[i - 1][j]  # entered mirror moving right -> turn down

        return (R[m - 1][n - 1] + D[m - 1][n - 1]) % MOD
```
