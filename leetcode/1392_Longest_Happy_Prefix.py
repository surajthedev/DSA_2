# A string is called a happy prefix if it is a non-empty prefix which is also a suffix (excluding itself).

# Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.



# Example 1:

# Input: s = "level"
# Output: "l"
# Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
# Example 2:

# Input: s = "ababab"
# Output: "abab"
# Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.


# Constraints:

# 1 <= s.length <= 105
# s contains only lowercase English letters.
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
# ### Brute Force Approach

python

```python
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)

        for i in range(n - 1, 0, -1):
            if s[:i] == s[n - i:]:
                return s[:i]

        return ""
```

### Optimal Approach (KMP / LPS Array)

python

```python
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * n

        length = 0
        i = 1

        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1

            elif length > 0:
                length = lps[length - 1]

            else:
                lps[i] = 0
                i += 1

        return s[:lps[-1]]
```
