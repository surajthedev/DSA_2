# Given the strings s1 and s2 of size n and the string evil, return the number of good strings.

# A good string has size n, it is alphabetically greater than or equal to s1, it is alphabetically smaller than or equal to s2, and it does not contain the string evil as a substring. Since the answer can be a huge number, return this modulo 109 + 7.



# Example 1:

# Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
# Output: 51
# Explanation: There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da".
# Example 2:

# Input: n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
# Output: 0
# Explanation: All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix "leet", therefore, there is not any good string.
# Example 3:

# Input: n = 2, s1 = "gx", s2 = "gz", evil = "x"
# Output: 2


# Constraints:

# s1.length == n
# s2.length == n
# s1 <= s2
# 1 <= n <= 500
# 1 <= evil.length <= 50
# All strings consist of lowercase English letters.
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
# ## 1. Brute Force Approach (Not Feasible for Constraints)

python

```python
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        count = 0

        def generate(curr):
            nonlocal count

            if len(curr) == n:
                if s1 <= curr <= s2 and evil not in curr:
                    count += 1
                return

            for ch in range(26):
                generate(curr + chr(ord('a') + ch))

        generate("")
        return count % MOD
```

Time Complexity: $O(26^n \cdot n)$

Space Complexity: $O(n)$

## 2. Optimal Approach (Digit DP + KMP)

python

```python
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        m = len(evil)

        # Build KMP LPS array
        lps = [0] * m
        j = 0

        for i in range(1, m):
            while j > 0 and evil[i] != evil[j]:
                j = lps[j - 1]

            if evil[i] == evil[j]:
                j += 1

            lps[i] = j

        # KMP transitions
        nxt = [[0] * 26 for _ in range(m)]

        for state in range(m):
            for c in range(26):
                ch = chr(c + ord('a'))
                j = state

                while j > 0 and evil[j] != ch:
                    j = lps[j - 1]

                if evil[j] == ch:
                    j += 1

                nxt[state][c] = j

        # DP with memoization
        from functools import lru_cache

        @lru_cache(None)
        def dp(pos, matched, tight1, tight2):
            if matched == m:
                return 0

            if pos == n:
                return 1

            low = ord(s1[pos]) - ord('a') if tight1 else 0
            high = ord(s2[pos]) - ord('a') if tight2 else 25

            ans = 0

            for c in range(low, high + 1):
                new_matched = nxt[matched][c]

                if new_matched == m:
                    continue

                ans += dp(
                    pos + 1,
                    new_matched,
                    tight1 and (c == low),
                    tight2 and (c == high)
                )

            return ans % MOD

        return dp(0, 0, True, True)
```

Time Complexity: $O(n \times |evil| \times 26)$

Space Complexity: $O(n \times |evil|)$

Optimal Solution Digit DP + KMP.
