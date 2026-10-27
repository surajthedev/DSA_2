# Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself (i.e. it can be written as a + a where a is some string).



# Example 1:

# Input: text = "abcabcabc"
# Output: 3
# Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".
# Example 2:

# Input: text = "leetcodeleetcode"
# Output: 2
# Explanation: The 2 substrings are "ee" and "leetcodeleetcode".


# Constraints:

# 1 <= text.length <= 2000
# text has only lowercase English letters.
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
#  ### Brute Force

python

```
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        result = set()

        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = text[i:j]
                length = len(sub)

                if length % 2 == 0:
                    half = length // 2
                    if sub[:half] == sub[half:]:
                        result.add(sub)

        return len(result)
```

### Optimal

python

```
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        result = set()

        for length in range(1, n // 2 + 1):
            for i in range(n - 2 * length + 1):
                if text[i:i + length] == text[i + length:i + 2 * length]:
                    result.add(text[i:i + 2 * length])

        return len(result)
```
