# Given a string s and an integer k, return true if you can use all the characters in s to construct non-empty k palindrome strings or false otherwise.



# Example 1:

# Input: s = "annabelle", k = 2
# Output: true
# Explanation: You can construct two palindromes using all characters in s.
# Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
# Example 2:

# Input: s = "leetcode", k = 3
# Output: false
# Explanation: It is impossible to construct 3 palindromes using all the characters of s.
# Example 3:

# Input: s = "true", k = 4
# Output: true
# Explanation: The only possible solution is to put each character in a separate string.


# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= 105
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
# ## 1. Brute Force Approach (Frequency Count)

python

```python
from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        freq = Counter(s)
        odd_count = 0

        for count in freq.values():
            if count % 2 != 0:
                odd_count += 1

        return odd_count <= k
```

Time Complexity: $O(n)$ Space Complexity: $O(1)$ — at most 26 characters.

## 2. Optimal Approach (Bitmask)

python

```python
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        mask = 0

        for ch in s:
            mask ^= (1 << (ord(ch) - ord('a')))

        odd_count = mask.bit_count()

        return odd_count <= k
```

Time Complexity: $O(n)$ Space Complexity: $O(1)$

Optimal Solution
