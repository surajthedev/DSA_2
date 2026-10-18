# Given a string s, return the last substring of s in lexicographical order.



# Example 1:

# Input: s = "abab"
# Output: "bab"
# Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
# Example 2:

# Input: s = "leetcode"
# Output: "tcode"


# Constraints:

# 1 <= s.length <= 4 * 105
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
# ### 1. Brute Force

python
```
class Solution:
    def lastSubstring(self, s: str) -> str:
        substrings = [s[i:] for i in range(len(s))]
        return max(substrings)
```

### 2. Optimal Solution — Two Pointers (O(n))

python
```
class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        i, j, k = 0, 1, 0

        while j + k < n:
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] < s[j + k]:
                i = max(i + k + 1, j)
                j = i + 1
                k = 0
            else:
                j = j + k + 1
                k = 0

        return s[i:]
```
