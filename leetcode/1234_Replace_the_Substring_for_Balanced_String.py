# You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.

# A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

# Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.



# Example 1:

# Input: s = "QWER"
# Output: 0
# Explanation: s is already balanced.
# Example 2:

# Input: s = "QQWE"
# Output: 1
# Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
# Example 3:

# Input: s = "QQQW"
# Output: 2
# Explanation: We can replace the first "QQ" to "ER".


# Constraints:

# n == s.length
# 4 <= n <= 105
# n is a multiple of 4.
# s contains only 'Q', 'W', 'E', and 'R'.
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
# ### Optimal Solution — Sliding Window

python
```
class Solution:
    def balancedString(self, s: str) -> int:
        from collections import Counter

        n = len(s)
        limit = n // 4
        count = Counter(s)

        if all(count[c] == limit for c in "QWER"):
            return 0

        left = 0
        ans = n

        for right in range(n):
            count[s[right]] -= 1

            while all(count[c] <= limit for c in "QWER"):
                ans = min(ans, right - left + 1)
                count[s[left]] += 1
                left += 1

        return ans
```

### Brute Force Solution

python
```
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        limit = n // 4

        for length in range(1, n + 1):
            for left in range(n - length + 1):
                window = s[left:left + length]
                remaining = s[:left] + s[left + length:]

                if all(remaining.count(c) <= limit for c in "QWER"):
                    return length

        return 0
```
