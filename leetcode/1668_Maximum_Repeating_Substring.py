# For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

# Given strings sequence and word, return the maximum k-repeating value of word in sequence.



# Example 1:

# Input: sequence = "ababc", word = "ab"
# Output: 2
# Explanation: "abab" is a substring in "ababc".
# Example 2:

# Input: sequence = "ababc", word = "ba"
# Output: 1
# Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".
# Example 3:

# Input: sequence = "ababc", word = "ac"
# Output: 0
# Explanation: "ac" is not a substring in "ababc".


# Constraints:

# 1 <= sequence.length <= 100
# 1 <= word.length <= 100
# sequence and word contains only lowercase English letters.
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
# ### 1. Brute Force Approach

Time: O(N × K × M) | Space: O(1)

python

```python
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        k = 1

        while word * k in sequence:
            ans = k
            k += 1

        return ans
```

### 2. Optimal Approach

Time: O(N × M) | Space: O(N)

python

```python
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)

        dp = [0] * (n + 1)
        ans = 0

        for i in range(m, n + 1):
            if sequence[i - m:i] == word:
                dp[i] = dp[i - m] + 1
                ans = max(ans, dp[i])

        return ans
```
