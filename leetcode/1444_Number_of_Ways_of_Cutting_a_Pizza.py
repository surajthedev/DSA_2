# Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts.

# For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

# Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.



# Example 1:



# Input: pizza = ["A..","AAA","..."], k = 3
# Output: 3
# Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
# Example 2:

# Input: pizza = ["A..","AA.","..."], k = 3
# Output: 1
# Example 3:

# Input: pizza = ["A..","A..","..."], k = 1
# Output: 1


# Constraints:

# 1 <= rows, cols <= 50
# rows == pizza.length
# cols == pizza[i].length
# 1 <= k <= 10
# pizza consists of characters 'A' and '.' only.
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
# ### 1. Brute Force Approach — Recursion

python

```python
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        rows, cols = len(pizza), len(pizza[0])

        def count(r, c):
            return sum(
                pizza[i][j] == 'A'
                for i in range(r, rows)
                for j in range(c, cols)
            )

        def dfs(r, c, pieces):
            if pieces == 1:
                return 1 if count(r, c) > 0 else 0

            ans = 0

            for i in range(r + 1, rows):
                if count(r, c) > count(i, c):
                    ans += dfs(i, c, pieces - 1)

            for j in range(c + 1, cols):
                if count(r, c) > count(r, j):
                    ans += dfs(r, j, pieces - 1)

            return ans % MOD

        return dfs(0, 0, k)
```

Time Complexity: Exponential

Space Complexity: O(k)

### 2. Optimal Approach — 3D DP + Prefix Sum

python

```python
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(pizza), len(pizza[0])

        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                prefix[i][j] = (
                    (pizza[i][j] == 'A')
                    + prefix[i + 1][j]
                    + prefix[i][j + 1]
                    - prefix[i + 1][j + 1]
                )

        dp = [[[0] * n for _ in range(m)] for _ in range(k + 1)]

        for i in range(m):
            for j in range(n):
                dp[1][i][j] = 1 if prefix[i][j] > 0 else 0

        for pieces in range(2, k + 1):
            for i in range(m):
                for j in range(n):

                    if prefix[i][j] < pieces:
                        continue

                    for r in range(i + 1, m):
                        if prefix[i][j] > prefix[r][j]:
                            dp[pieces][i][j] += dp[pieces - 1][r][j]

                    for c in range(j + 1, n):
                        if prefix[i][j] > prefix[i][c]:
                            dp[pieces][i][j] += dp[pieces - 1][i][c]

                    dp[pieces][i][j] %= MOD

        return dp[k][0][0]
```

Time Complexity: O(k × m × n × (m + n))

Space Complexity: O(k × m × n)
