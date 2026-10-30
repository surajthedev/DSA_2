# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.



# Example 1:

# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
# Example 2:

# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
# Example 3:

# Input: s = "abc"
# Output: 1


# Constraints:

# 3 <= s.length <= 5 x 104
# s only consists of 'a', 'b' or 'c' characters.
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
# ### 1. Brute Force – O(n²)

python

```
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            freq = [0] * 3

            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1

                if freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
                    ans += 1

        return ans
```

### 2. Optimal – Sliding Window – O(n)

python

```
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        freq = [0] * 3

        left = 0
        ans = 0

        for right in range(n):
            freq[ord(s[right]) - ord('a')] += 1

            while freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
                ans += n - right

                freq[ord(s[left]) - ord('a')] -= 1
                left += 1

        return ans
```
