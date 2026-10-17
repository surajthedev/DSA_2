# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.



# Example 1:


# Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
# Example 2:


# Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.


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
#
#
#
#
# ### Brute Force — Python

python
```
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        land = []

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    land.append((i, j))

        if not land or len(land) == n * n:
            return -1

        ans = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    dist = min(
                        abs(i - x) + abs(j - y)
                        for x, y in land
                    )
                    ans = max(ans, dist)

        return ans
```

### Optimal — Python (Multi-source BFS)

python
```
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        if not queue or len(queue) == n * n:
            return -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        distance = -1

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < n and 0 <= ny < n
                            and grid[nx][ny] == 0):
                        grid[nx][ny] = 1
                        queue.append((nx, ny))

            distance += 1

        return distance
```
