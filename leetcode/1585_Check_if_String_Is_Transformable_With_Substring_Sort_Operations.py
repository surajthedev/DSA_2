# Given two strings s and t, transform string s into string t using the following operation any number of times:

# Choose a non-empty substring in s and sort it in place so the characters are in ascending order.
# For example, applying the operation on the underlined substring in "14234" results in "12344".
# Return true if it is possible to transform s into t. Otherwise, return false.

# A substring is a contiguous sequence of characters within a string.



# Example 1:

# Input: s = "84532", t = "34852"
# Output: true
# Explanation: You can transform s into t using the following sort operations:
# "84532" (from index 2 to 3) -> "84352"
# "84352" (from index 0 to 2) -> "34852"
# Example 2:

# Input: s = "34521", t = "23415"
# Output: true
# Explanation: You can transform s into t using the following sort operations:
# "34521" -> "23451"
# "23451" -> "23415"
# Example 3:

# Input: s = "12345", t = "12435"
# Output: false


# Constraints:

# s.length == t.length
# 1 <= s.length <= 105
# s and t consist of only digits.
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
# ### **1. Brute Force — Not Efficient**

```
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        if sorted(s) != sorted(t):
            return False

        s = list(s)

        for i in range(len(t)):
            if s[i] == t[i]:
                continue

            j = i + 1

            while j < len(s) and s[j] != t[i]:
                if s[j] < t[i]:
                    return False
                j += 1

            if j == len(s):
                return False

            s[i:j + 1] = sorted(s[i:j + 1])

        return True```

### **2. Optimal — O(n)**

```
from collections import deque

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = [deque() for _ in range(10)]

        for i, ch in enumerate(s):
            pos[int(ch)].append(i)

        for ch in t:
            digit = int(ch)

            if not pos[digit]:
                return False

            idx = pos[digit][0]

            for smaller in range(digit):
                if pos[smaller] and pos[smaller][0] < idx:
                    return False

            pos[digit].popleft()

        return True```
