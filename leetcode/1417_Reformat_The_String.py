# You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

# You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

# Return the reformatted string or return an empty string if it is impossible to reformat the string.



# Example 1:

# Input: s = "a0b1c2"
# Output: "0a1b2c"
# Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
# Example 2:

# Input: s = "leetcode"
# Output: ""
# Explanation: "leetcode" has only characters so we cannot separate them by digits.
# Example 3:

# Input: s = "1229857369"
# Output: ""
# Explanation: "1229857369" has only digits so we cannot separate them by characters.


# Constraints:

# 1 <= s.length <= 500
# s consists of only lowercase English letters and/or digits.
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
    def reformat(self, s: str) -> str:
        from itertools import permutations

        for p in permutations(s):
            valid = True

            for i in range(1, len(p)):
                if p[i].isdigit() == p[i - 1].isdigit():
                    valid = False
                    break

            if valid:
                return ''.join(p)

        return ""
```

Time Complexity: $O(n! \times n)$

Space Complexity: $O(n)$ (excluding permutation generation overhead).

### 2. Optimal Approach

python

```python
class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []

        for ch in s:
            if ch.isdigit():
                digits.append(ch)
            else:
                letters.append(ch)

        if abs(len(letters) - len(digits)) > 1:
            return ""

        result = []

        if len(letters) > len(digits):
            first, second = letters, digits
        else:
            first, second = digits, letters

        for i in range(len(second)):
            result.append(first[i])
            result.append(second[i])

        if len(first) > len(second):
            result.append(first[-1])

        return ''.join(result)
```

Time Complexity: $O(n)$

Space Complexity: $O(n)$
