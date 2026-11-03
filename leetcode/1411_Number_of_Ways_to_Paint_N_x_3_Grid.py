# You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

# Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.



# Example 1:


# Input: n = 1
# Output: 12
# Explanation: There are 12 possible way to paint the grid as shown.
# Example 2:

# Input: n = 5000
# Output: 30228214


# Constraints:

# n == grid.length
# 1 <= n <= 5000
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
# ### Brute Force (Backtracking + Memoization)

python

```python
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        patterns = []

        for a in range(3):
            for b in range(3):
                for c in range(3):
                    if a != b and b != c:
                        patterns.append((a, b, c))

        dp = {}

        def solve(row, prev):
            if row == n:
                return 1

            key = (row, prev)

            if key in dp:
                return dp[key]

            ans = 0

            for curr in patterns:
                if all(curr[i] != prev[i] for i in range(3)):
                    ans += solve(row + 1, curr)

            dp[key] = ans % MOD
            return dp[key]

        return solve(0, (-1, -1, -1))
```

### Optimal (Dynamic Programming)

python

```python
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        aba = 6
        abc = 6

        for _ in range(2, n + 1):
            new_aba = (3 * aba + 2 * abc) % MOD
            new_abc = (2 * aba + 2 * abc) % MOD

            aba, abc = new_aba, new_abc

        return (aba + abc) % MOD
```
