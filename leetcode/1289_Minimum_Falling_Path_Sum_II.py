# Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

# A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.



# Example 1:


# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 13
# Explanation:
# The possible falling paths are:
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# The falling path with the smallest sum is [1,5,7], so the answer is 13.
# Example 2:

# Input: grid = [[7]]
# Output: 7


# Constraints:

# n == grid.length == grid[i].length
# 1 <= n <= 200
# -99 <= grid[i][j] <= 99
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
# ### Brute Force (Recursion + Memoization)

python

```

from functools import lru_cache

class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)

        @lru_cache(None)
        def dfs(row, col):
            if row == n - 1:
                return grid[row][col]

            ans = float('inf')

            for next_col in range(n):
                if next_col != col:
                    ans = min(ans, dfs(row + 1, next_col))

            return grid[row][col] + ans

        return min(dfs(0, col) for col in range(n))
```

### Optimal (Dynamic Programming)

python

```

class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dp = grid[0][:]

        for row in range(1, n):
            min1 = min(dp)
            idx = dp.index(min1)
            min2 = min(dp[:idx] + dp[idx + 1:]) if n > 1 else float('inf')

            new_dp = [0] * n

            for col in range(n):
                best = min2 if col == idx else min1
                new_dp[col] = grid[row][col] + best

            dp = new_dp

        return min(dp)
```
