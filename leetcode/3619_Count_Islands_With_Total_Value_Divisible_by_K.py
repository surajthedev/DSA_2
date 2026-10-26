# You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).

# The total value of an island is the sum of the values of all cells in the island.

# Return the number of islands with a total value divisible by k.



# Example 1:


# Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5

# Output: 2

# Explanation:

# The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

# Example 2:


# Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3

# Output: 6

# Explanation:

# The grid contains six islands, each with a total value that is divisible by 3.



# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 105
# 0 <= grid[i][j] <= 106
# 1 <= k <= 106
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
# Brute force:
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        ans = 0

        def dfs(r, c):
            visited[r][c] = True
            total = grid[r][c]

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if (0 <= nr < m and 0 <= nc < n
                    and grid[nr][nc] > 0
                    and not visited[nr][nc]):
                    total += dfs(nr, nc)

            return total

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    if dfs(i, j) % k == 0:
                        ans += 1

        return ans












# Optimal:
from typing import List
from collections import deque

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    total = 0
                    q = deque([(i, j)])
                    total += grid[i][j]
                    grid[i][j] = 0  # mark visited in-place
                    while q:
                        x, y = q.popleft()
                        for dx, dy in dirs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                                total += grid[nx][ny]
                                grid[nx][ny] = 0
                                q.append((nx, ny))
                    if total % k == 0:
                        count += 1
        return count
