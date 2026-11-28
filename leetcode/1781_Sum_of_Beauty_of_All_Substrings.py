# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.



# Example 1:

# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
# Example 2:

# Input: s = "aabcbaa"
# Output: 17


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
#
#
#
#
#
#
#
# ### 1. Brute Force — O(n³)

python

```python
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                sub = s[i:j + 1]
                freq = {}

                for ch in sub:
                    freq[ch] = freq.get(ch, 0) + 1

                ans += max(freq.values()) - min(freq.values())

        return ans
```

### 2. Optimal — O(n² × 26)

python

```python
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            freq = [0] * 26

            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1

                mx = max(freq)
                mn = min(x for x in freq if x > 0)

                ans += mx - mn

        return ans
```
