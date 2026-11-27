# You are given two strings, word1 and word2. You want to construct a string in the following manner:

# Choose some non-empty subsequence subsequence1 from word1.
# Choose some non-empty subsequence subsequence2 from word2.
# Concatenate the subsequences: subsequence1 + subsequence2, to make the string.
# Return the length of the longest palindrome that can be constructed in the described manner. If no palindromes can be constructed, return 0.

# A subsequence of a string s is a string that can be made by deleting some (possibly none) characters from s without changing the order of the remaining characters.

# A palindrome is a string that reads the same forward as well as backward.



# Example 1:

# Input: word1 = "cacb", word2 = "cbba"
# Output: 5
# Explanation: Choose "ab" from word1 and "cba" from word2 to make "abcba", which is a palindrome.
# Example 2:

# Input: word1 = "ab", word2 = "ab"
# Output: 3
# Explanation: Choose "ab" from word1 and "a" from word2 to make "aba", which is a palindrome.
# Example 3:

# Input: word1 = "aa", word2 = "bb"
# Output: 0
# Explanation: You cannot construct a palindrome from the described method, so return 0.


# Constraints:

# 1 <= word1.length, word2.length <= 1000
# word1 and word2 consist of lowercase English letters.
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
# ### 1. Brute Force Approach

Time Complexity: Exponential — $O(2^{n+m})$

python

```python
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        from itertools import combinations

        ans = 0

        for i in range(1, len(word1) + 1):
            for a in combinations(word1, i):
                s1 = ''.join(a)

                for j in range(1, len(word2) + 1):
                    for b in combinations(word2, j):
                        s = s1 + ''.join(b)

                        if s == s[::-1]:
                            ans = max(ans, len(s))

        return ans
```

### 2. Optimal Approach (Dynamic Programming – LCS / Longest Palindromic Subsequence)

O((n + m)²) Time | O((n + m)²) Spacepython

```python
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n = len(s)
        m = len(word1)

        dp = [[0] * n for _ in range(n)]

        ans = 0

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1] if i + 1 <= j - 1 else 2

                    if i < m <= j:
                        ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return ans
```
