# Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

# A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

# Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

# Return true if any cycle of the same value exists in grid, otherwise, return false.



# Example 1:



# Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# Output: true
# Explanation: There are two valid cycles shown in different colors in the image below:

# Example 2:



# Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
# Output: true
# Explanation: There is only one valid cycle highlighted in the image below:

# Example 3:



# Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
# Output: false


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid consists only of lowercase English letters.
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
# ### Brute Force — DFS (O((m × n)²))

python

```python
from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = set()

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c, pr, pc, path):
            visited.add((r, c))
            path.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if grid[nr][nc] != grid[r][c]:
                    continue

                if (nr, nc) == (pr, pc):
                    continue

                if (nr, nc) in path:
                    return True

                if (nr, nc) not in visited:
                    if dfs(nr, nc, r, c, path):
                        return True

            path.remove((r, c))
            return False

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    if dfs(i, j, -1, -1, set()):
                        return True

        return False
```

### Optimal — DFS (O(m × n) Time, O(m × n) Space)

python

```python
from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, pr, pc):
            visited[r][c] = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if grid[nr][nc] != grid[r][c]:
                    continue

                if nr == pr and nc == pc:
                    continue

                if visited[nr][nc]:
                    return True

                if dfs(nr, nc, r, c):
                    return True

            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1):
                        return True

        return False
```
