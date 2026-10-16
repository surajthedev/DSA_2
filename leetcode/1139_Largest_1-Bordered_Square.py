# Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.



# Example 1:

# Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
# Output: 9
# Example 2:

# Input: grid = [[1,1,0,0]]
# Output: 1


# Constraints:

# 1 <= grid.length <= 100
# 1 <= grid[0].length <= 100
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
# ### Brute Force — O(m × n × min(m,n)³)

python
```
from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for size in range(min(m, n), 0, -1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    if (
                        all(grid[i][c] == 1 for c in range(j, j + size))
                        and all(grid[i + size - 1][c] == 1 for c in range(j, j + size))
                        and all(grid[r][j] == 1 for r in range(i, i + size))
                        and all(grid[r][j + size - 1] == 1 for r in range(i, i + size))
                    ):
                        return size * size

        return 0
```

### Optimal — O(m × n × min(m,n))

python
```
from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        right = [[0] * (n + 1) for _ in range(m)]
        down = [[0] * n for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    right[i][j] = 1 + right[i][j + 1]
                    down[i][j] = 1 + down[i + 1][j]

        for size in range(min(m, n), 0, -1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    if (
                        right[i][j] >= size
                        and down[i][j] >= size
                        and right[i + size - 1][j] >= size
                        and down[i][j + size - 1] >= size
                    ):
                        return size * size

        return 0
```
