# You have a keyboard layout as shown above in the X-Y plane, where each English uppercase letter is located at some coordinate.

# For example, the letter 'A' is located at coordinate (0, 0), the letter 'B' is located at coordinate (0, 1), the letter 'P' is located at coordinate (2, 3) and the letter 'Z' is located at coordinate (4, 1).
# Given the string word, return the minimum total distance to type such string using only two fingers.

# The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.

# Note that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.



# Example 1:

# Input: word = "CAKE"
# Output: 3
# Explanation: Using two fingers, one optimal way to type "CAKE" is:
# Finger 1 on letter 'C' -> cost = 0
# Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2
# Finger 2 on letter 'K' -> cost = 0
# Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1
# Total distance = 3
# Example 2:

# Input: word = "HAPPY"
# Output: 6
# Explanation: Using two fingers, one optimal way to type "HAPPY" is:
# Finger 1 on letter 'H' -> cost = 0
# Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
# Finger 2 on letter 'P' -> cost = 0
# Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
# Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
# Total distance = 6


# Constraints:

# 2 <= word.length <= 300
# word consists of uppercase English letters.
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
# ### Brute Force (Dynamic Programming)

python

```
from functools import lru_cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)

        def dist(a, b):
            if a == 26 or b == 26:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        @lru_cache(None)
        def dp(i, f1, f2):
            if i == n:
                return 0

            cur = ord(word[i]) - ord('A')

            move1 = dist(f1, cur) + dp(i + 1, cur, f2)
            move2 = dist(f2, cur) + dp(i + 1, f1, cur)

            return min(move1, move2)

        return dp(0, 26, 26)
```

### Optimal (Dynamic Programming)

python

```
class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            if a == -1:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        INF = float('inf')
        # dp[j] = min cost where one finger is on the last typed letter,
        # and the other finger is at letter j (26 = not placed yet)
        dp = [INF] * 27
        dp[26] = 0
        prev = ord(word[0]) - 65

        for i in range(1, len(word)):
            cur = ord(word[i]) - 65
            ndp = [INF] * 27
            for j in range(27):
                if dp[j] == INF:
                    continue
                # same finger moves prev -> cur, other finger stays at j
                ndp[j] = min(ndp[j], dp[j] + dist(prev, cur))
                # other finger (at j) moves to cur, prev finger becomes the "other"
                other = -1 if j == 26 else j
                ndp[prev] = min(ndp[prev], dp[j] + dist(other, cur))
            dp = ndp
            prev = cur

        return min(dp)
```
