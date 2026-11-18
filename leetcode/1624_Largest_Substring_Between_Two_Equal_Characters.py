# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.



# Example 1:

# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.
# Example 2:

# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".
# Example 3:

# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.


# Constraints:

# 1 <= s.length <= 300
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
#
#
#
# ### 1. Brute Force Approach

python

```python
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        n = len(s)

        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    ans = max(ans, j - i - 1)

        return ans
```

### 2. Optimal Approach (HashMap)

python

```python
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        ans = -1

        for i, ch in enumerate(s):
            if ch in first:
                ans = max(ans, i - first[ch] - 1)
            else:
                first[ch] = i

        return ans
```
