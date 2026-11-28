# Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.



# Example 1:

# Input: s = "1001"
# Output: false
# Explanation: The string has two segments of size 1.
# Example 2:

# Input: s = "110"
# Output: true


# Constraints:

# 1 <= s.length <= 100
# s[i]​​​​ is either '0' or '1'.
# s[0] is '1'.
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
# ### 1. Brute Force — O(n²)

python

```python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        segments = 0

        for i in range(len(s)):
            if s[i] == '1' and (i == 0 or s[i - 1] == '0'):
                segments += 1

        return segments <= 1
```

### 2. Optimal — O(n)

python

```python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s
```
