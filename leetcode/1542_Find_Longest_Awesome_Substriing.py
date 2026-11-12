# You are given a string s. An awesome substring is a non-empty substring of s such that we can make any number of swaps in order to make it a palindrome.

# Return the length of the maximum length awesome substring of s.



# Example 1:

# Input: s = "3242415"
# Output: 5
# Explanation: "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.
# Example 2:

# Input: s = "12345678"
# Output: 1
# Example 3:

# Input: s = "213123"
# Output: 6
# Explanation: "213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.


# Constraints:

# 1 <= s.length <= 105
# s consists only of digits.
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
# ### 1. Brute Force – O(n² × 10)

python

```python
class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        ans = 1

        for i in range(n):
            mask = 0

            for j in range(i, n):
                digit = int(s[j])
                mask ^= (1 << digit)

                if mask == 0 or (mask & (mask - 1)) == 0:
                    ans = max(ans, j - i + 1)

        return ans
```

### 2. Optimal – Bitmask + Prefix XOR + HashMap

Time Complexity: O(10 × n) = O(n) Space Complexity: O(1) (fixed 10 digits)

python

```python
class Solution:
    def longestAwesome(self, s: str) -> int:
        mask = 0
        ans = 0

        first = {0: -1}

        for i, ch in enumerate(s):
            digit = int(ch)
            mask ^= (1 << digit)

            if mask in first:
                ans = max(ans, i - first[mask])

            for d in range(10):
                new_mask = mask ^ (1 << d)

                if new_mask in first:
                    ans = max(ans, i - first[new_mask])

            if mask not in first:
                first[mask] = i

        return ans
```
