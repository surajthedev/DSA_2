# You are given a list of strings of the same length words and a string target.

# Your task is to form target using the given words under the following rules:

# target should be formed from left to right.
# To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
# Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
# Repeat the process until you form the string target.
# Notice that you can use multiple characters from the same string in words provided the conditions above are met.

# Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.



# Example 1:

# Input: words = ["acca","bbbb","caca"], target = "aba"
# Output: 6
# Explanation: There are 6 ways to form target.
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
# Example 2:

# Input: words = ["abba","baab"], target = "bab"
# Output: 4
# Explanation: There are 4 ways to form target.
# "bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
# "bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
# "bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
# "bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")


# Constraints:

# 1 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# All strings in words have the same length.
# 1 <= target.length <= 1000
# words[i] and target contain only lowercase English letters.
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
# ### 1. Brute Force Solution (Recursive + Memoization)

python

```python
from typing import List
from functools import lru_cache

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m = len(words[0])
        n = len(target)

        freq = [[0] * 26 for _ in range(m)]

        for word in words:
            for j, ch in enumerate(word):
                freq[j][ord(ch) - ord('a')] += 1

        @lru_cache(None)
        def solve(i, j):
            if i == n:
                return 1
            if j == m:
                return 0

            ans = solve(i, j + 1)

            count = freq[j][ord(target[i]) - ord('a')]

            if count:
                ans += count * solve(i + 1, j + 1)

            return ans % MOD

        return solve(0, 0)
```

Time Complexity: O(m × n + 26 × m)

Space Complexity: O(m × n)

### 2. Optimal Solution (Dynamic Programming)

python

```python
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7

        m = len(words[0])
        n = len(target)

        freq = [[0] * 26 for _ in range(m)]

        for word in words:
            for j, ch in enumerate(word):
                freq[j][ord(ch) - ord('a')] += 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for j in range(m):
            for i in range(n - 1, -1, -1):
                count = freq[j][ord(target[i]) - ord('a')]

                dp[i + 1] = (
                    dp[i + 1] + dp[i] * count
                ) % MOD

        return dp[n]
```

Time Complexity: O(words.length × word.length + target.length × word.length)

Space Complexity: O(26 × word.length + target.length)
