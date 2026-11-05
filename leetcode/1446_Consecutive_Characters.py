# The power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Given a string s, return the power of s.



# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# Example 2:

# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.


# Constraints:

# 1 <= s.length <= 500
# s consists of only lowercase English letters.
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
    def maxPower(self, s: str) -> int:
        ans = 1
        n = len(s)

        for i in range(n):
            count = 1

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    count += 1
                else:
                    break

            ans = max(ans, count)

        return ans
```

Time Complexity: O(n²)

Space Complexity: O(1)

### 2. Optimal Approach — Single Pass

python

```python
class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1

            ans = max(ans, count)

        return ans
```

Time Complexity: O(n)

Space Complexity: O(1)
