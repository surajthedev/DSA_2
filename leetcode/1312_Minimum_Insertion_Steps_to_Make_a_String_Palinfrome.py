# Given a string s. In one step you can insert any character at any index of the string.

# Return the minimum number of steps to make s palindrome.

# A Palindrome String is one that reads the same backward as well as forward.



# Example 1:

# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we do not need any insertions.
# Example 2:

# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".
# Example 3:

# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".


# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.
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
# ### 1. Brute Force (Recursion + Memoization)

python

```
from functools import lru_cache

class Solution:
    def minInsertions(self, s: str) -> int:
        @lru_cache(None)
        def solve(i, j):
            if i >= j:
                return 0

            if s[i] == s[j]:
                return solve(i + 1, j - 1)

            return 1 + min(
                solve(i + 1, j),
                solve(i, j - 1)
            )

        return solve(0, len(s) - 1)
```

### 2. Optimal (Dynamic Programming — O(n²))

python

```
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] if length > 2 else 0
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
```
