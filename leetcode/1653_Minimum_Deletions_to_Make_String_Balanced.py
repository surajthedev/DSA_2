# You are given a string s consisting only of characters 'a' and 'b'​​​​.

# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

# Return the minimum number of deletions needed to make s balanced.



# Example 1:

# Input: s = "aababbab"
# Output: 2
# Explanation: You can either:
# Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
# Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
# Example 2:

# Input: s = "bbaaaaabb"
# Output: 2
# Explanation: The only solution is to delete the first two characters.


# Constraints:

# 1 <= s.length <= 105
# s[i] is 'a' or 'b'​​.
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
# ### Brute Force — O(n²)

python

```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        ans = n

        for i in range(n + 1):
            left = s[:i]
            right = s[i:]

            deletions = left.count('b') + right.count('a')
            ans = min(ans, deletions)

        return ans
```

### Optimal Approach — Dynamic Programming — O(n)

python

```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = 0
        count_b = 0

        for ch in s:
            if ch == 'b':
                count_b += 1
            else:
                dp = min(dp + 1, count_b)

        return dp
```
