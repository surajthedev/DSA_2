# Given two strings s and t, find the number of ways you can choose a non-empty substring of s and replace a single character by a different character such that the resulting substring is a substring of t. In other words, find the number of substrings in s that differ from some substring in t by exactly one character.

# For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a', so this is a valid way.

# Return the number of substrings that satisfy the condition above.

# A substring is a contiguous sequence of characters within a string.



# Example 1:

# Input: s = "aba", t = "baba"
# Output: 6
# Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# The underlined portions are the substrings that are chosen from s and t.
# ​​Example 2:
# Input: s = "ab", t = "bb"
# Output: 3
# Explanation: The following are the pairs of substrings from s and t that differ by 1 character:
# ("ab", "bb")
# ("ab", "bb")
# ("ab", "bb")
# ​​​​The underlined portions are the substrings that are chosen from s and t.


# Constraints:

# 1 <= s.length, t.length <= 100
# s and t consist of lowercase English letters only.
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
# Sorry, previous DP solution mein bug tha. Ye corrected solutions hain.

### 1. Brute Force Solution

python

```python
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0

        for i in range(len(s)):
            for j in range(len(t)):
                diff = 0

                for k in range(min(len(s) - i, len(t) - j)):
                    if s[i + k] != t[j + k]:
                        diff += 1

                    if diff == 1:
                        ans += 1
                    elif diff > 1:
                        break

        return ans
```

Time Complexity: O(n × m × min(n, m))

### 2. Optimal Solution (DP)

python

```python
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]

        for i in range(n):
            for j in range(m):
                if s[i] != t[j]:
                    left = 0
                    right = dp[i + 1][j + 1]

                    x, y = i - 1, j - 1

                    while x >= 0 and y >= 0 and s[x] == t[y]:
                        left += 1
                        x -= 1
                        y -= 1

                    ans += (left + 1) * (right + 1)

        return ans
```

Time Complexity: O(n × m × min(n, m))

Space Complexity: O(n × m)

### Test cases

python

```python
s = "aba"
t = "baba"
# Output: 6

s = "ab"
t = "bb"
# Output: 3

s = "abe"
t = "bbc"
# Output: 10
```
