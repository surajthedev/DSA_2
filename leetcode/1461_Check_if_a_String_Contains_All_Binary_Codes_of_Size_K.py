# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.



# Example 1:

# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
# Example 2:

# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.
# Example 3:

# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and does not exist in the array.


# Constraints:

# 1 <= s.length <= 5 * 105
# s[i] is either '0' or '1'.
# 1 <= k <= 20
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
# ## 1. Brute Force Solution

python

```python
from typing import *

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)

        for i in range(2 ** k):
            binary = format(i, f'0{k}b')

            if binary not in s:
                return False

        return True
```

Time: O(2^k × n) worst case

## 2. Optimal Solution (Sliding Window + Set)

python

```python
from typing import *

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        required = 1 << k

        if len(s) - k + 1 < required:
            return False

        seen = set()

        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])

            if len(seen) == required:
                return True

        return False
```

Time: O(n × k) Space: O(2^k × k)

## 3. More Optimal Solution (Bit Manipulation + Sliding Window)

python

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        required = 1 << k

        if len(s) - k + 1 < required:
            return False

        seen = set()
        num = 0
        mask = required - 1

        for i in range(len(s)):
            num = ((num << 1) & mask) | int(s[i])

            if i >= k - 1:
                seen.add(num)

                if len(seen) == required:
                    return True

        return False
```

Time: O(n) Space: O(2^k)
