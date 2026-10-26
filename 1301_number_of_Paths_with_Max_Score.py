# You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

# You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

# Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

# In case there is no path, return [0, 0].



# Example 1:

# Input: board = ["E23","2X2","12S"]
# Output: [7,1]
# Example 2:

# Input: board = ["E12","1X1","21S"]
# Output: [4,2]
# Example 3:

# Input: board = ["E11","XXX","11S"]
# Output: [0,0]


# Constraints:

# 2 <= board.length == board[i].length <= 100
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
# ### Brute Force (DFS + Memoization)

python

```
from functools import lru_cache

class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(r, c):
            if r < 0 or c < 0 or board[r][c] == 'X':
                return (-1, 0)

            if r == 0 and c == 0:
                return (0, 1)

            best = -1
            ways = 0

            for nr, nc in [(r - 1, c), (r, c - 1), (r - 1, c - 1)]:
                score, count = dfs(nr, nc)

                if count == 0:
                    continue

                if score > best:
                    best = score
                    ways = count
                elif score == best:
                    ways = (ways + count) % MOD

            if ways == 0:
                return (-1, 0)

            value = int(board[r][c]) if board[r][c].isdigit() else 0
            return (best + value, ways)

        score, ways = dfs(n - 1, n - 1)

        return [max(score, 0), ways] if ways else [0, 0]
```

### Optimal (Dynamic Programming)

class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        MOD = 10**9 + 7

        dp = [[(float("-inf"), 0) for _ in range(n + 1)] for _ in range(n + 1)]
        dp[n][n] = (0, 1)

        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == 'X':
                    continue

                if r == 0 and c == 0:
                    continue

                best = max(
                    dp[r + 1][c][0],
                    dp[r][c + 1][0],
                    dp[r + 1][c + 1][0]
                )

                if best == float("-inf"):
                    continue

                ways = 0
                for nr, nc in ((r + 1, c), (r, c + 1), (r + 1, c + 1)):
                    if dp[nr][nc][0] == best:
                        ways = (ways + dp[nr][nc][1]) % MOD

                value = int(board[r][c]) if board[r][c].isdigit() else 0
                dp[r][c] = (best + value, ways)

        best = max(dp[1][0][0], dp[0][1][0], dp[1][1][0])
        if best == float("-inf"):
            return [0, 0]

        ways = 0
        for r, c in ((1, 0), (0, 1), (1, 1)):
            if dp[r][c][0] == best:
                ways = (ways + dp[r][c][1]) % MOD

        value = int(board[0][0]) if board[0][0].isdigit() else 0
        return [best + value, ways]
