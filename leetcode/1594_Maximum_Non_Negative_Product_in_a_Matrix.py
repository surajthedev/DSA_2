# You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

# Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

# Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative, return -1.

# Notice that the modulo is performed after getting the maximum product.



# Example 1:


# Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
# Output: -1
# Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
# Example 2:


# Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
# Output: 8
# Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).
# Example 3:


# Input: grid = [[1,3],[0,-4]]
# Output: 0
# Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0).


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 15
# -4 <= grid[i][j] <= 4
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
# **Brute Force — DFS**

```
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return grid[i][j], grid[i][j]

            mn = float('inf')
            mx = float('-inf')

            if i + 1 < m:
                a, b = dfs(i + 1, j)
                mn = min(mn, a * grid[i][j], b * grid[i][j])
                mx = max(mx, a * grid[i][j], b * grid[i][j])

            if j + 1 < n:
                a, b = dfs(i, j + 1)
                mn = min(mn, a * grid[i][j], b * grid[i][j])
                mx = max(mx, a * grid[i][j], b * grid[i][j])

            return mn, mx

        mn, mx = dfs(0, 0)

        return mx % (10**9 + 7) if mx >= 0 else -1```

**Optimal — Dynamic Programming O(m × n)**

```
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp_min = [[0] * n for _ in range(m)]
        dp_max = [[0] * n for _ in range(m)]

        dp_min[0][0] = dp_max[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                val = grid[i][j]
                candidates = []

                if i > 0:
                    candidates.extend([
                        dp_min[i-1][j] * val,
                        dp_max[i-1][j] * val
                    ])

                if j > 0:
                    candidates.extend([
                        dp_min[i][j-1] * val,
                        dp_max[i][j-1] * val
                    ])

                dp_min[i][j] = min(candidates)
                dp_max[i][j] = max(candidates)

        ans = dp_max[m-1][n-1]

        return ans % MOD if ans >= 0 else -1```
