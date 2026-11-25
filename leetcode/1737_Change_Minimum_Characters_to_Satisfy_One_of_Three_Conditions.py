# You are given two strings a and b that consist of lowercase letters. In one operation, you can change any character in a or b to any lowercase letter.

# Your goal is to satisfy one of the following three conditions:

# Every letter in a is strictly less than every letter in b in the alphabet.
# Every letter in b is strictly less than every letter in a in the alphabet.
# Both a and b consist of only one distinct letter.
# Return the minimum number of operations needed to achieve your goal.



# Example 1:

# Input: a = "aba", b = "caa"
# Output: 2
# Explanation: Consider the best way to make each condition true:
# 1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
# 2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b is less than every letter in a.
# 3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
# The best way was done in 2 operations (either condition 1 or condition 3).
# Example 2:

# Input: a = "dabadd", b = "cda"
# Output: 3
# Explanation: The best way is to make condition 1 true by changing b to "eee".


# Constraints:

# 1 <= a.length, b.length <= 105
# a and b consist only of lowercase letters.
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
# ### 1. Brute Force — Python

python

```python

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        ans = float('inf')

        for i in range(26):
            x = chr(ord('a') + i)

            # Condition 3: Both strings have one distinct character
            changes = sum(c != x for c in a) + sum(c != x for c in b)
            ans = min(ans, changes)

            # Condition 1 and 2
            if i < 25:
                changes1 = sum(c > x for c in a) + sum(c <= x for c in b)
                changes2 = sum(c <= x for c in a) + sum(c > x for c in b)

                ans = min(ans, changes1, changes2)

        return ans
```

- Time Complexity: O(26 × (N + M))
- Space Complexity: O(1)

### 2. Optimal — Python

Recommendedpython

```python

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        ca = [0] * 26
        cb = [0] * 26

        for c in a:
            ca[ord(c) - ord('a')] += 1

        for c in b:
            cb[ord(c) - ord('a')] += 1

        n, m = len(a), len(b)

        ans = n + m - max(
            ca[i] + cb[i] for i in range(26)
        )

        for i in range(25):
            a_less = sum(ca[:i + 1])
            b_less = sum(cb[:i + 1])

            # Every character in a < every character in b
            ans = min(ans, n - a_less + b_less)

            # Every character in b < every character in a
            ans = min(ans, m - b_less + a_less)

        return ans
```

- Time Complexity: O(N + M + 26)
- Space Complexity: O(26) = O(1)
