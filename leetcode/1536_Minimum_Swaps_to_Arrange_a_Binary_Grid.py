# Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

# A grid is said to be valid if all the cells above the main diagonal are zeros.

# Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

# The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).



# Example 1:


# Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
# Output: 3
# Example 2:


# Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# Output: -1
# Explanation: All rows are similar, swaps have no effect on the grid.
# Example 3:


# Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
# Output: 0


# Constraints:

# n == grid.length == grid[i].length
# 1 <= n <= 200
# grid[i][j] is either 0 or 1
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
# ### 1. Brute Force – O(n³)

python

```python
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0

        for i in range(n):
            pos = -1

            for j in range(i, n):
                zeros = 0

                for k in range(n - 1, -1, -1):
                    if grid[j][k] == 1:
                        break
                    zeros += 1

                if zeros >= n - i - 1:
                    pos = j
                    break

            if pos == -1:
                return -1

            while pos > i:
                grid[pos], grid[pos - 1] = grid[pos - 1], grid[pos]
                pos -= 1
                ans += 1

        return ans
```

### 2. Optimal – O(n²) | O(n)

python

```python
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        zeros = []

        for row in grid:
            count = 0

            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break

            zeros.append(count)

        ans = 0

        for i in range(n):
            pos = i

            while pos < n and zeros[pos] < n - i - 1:
                pos += 1

            if pos == n:
                return -1

            while pos > i:
                zeros[pos], zeros[pos - 1] = zeros[pos - 1], zeros[pos]
                pos -= 1
                ans += 1

        return ans
```
