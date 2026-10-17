# You are given a string text. You can swap two of the characters in the text.

# Return the length of the longest substring with repeated characters.



# Example 1:

# Input: text = "ababa"
# Output: 3
# Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa" with length 3.
# Example 2:

# Input: text = "aaabaaa"
# Output: 6
# Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa" with length 6.
# Example 3:

# Input: text = "aaaaa"
# Output: 5
# Explanation: No need to swap, longest repeated character substring is "aaaaa" with length is 5.


# Constraints:

# 1 <= text.length <= 2 * 104
# text consist of lowercase English characters only.
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
# ### Brute Force — Python

python
```
from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        n = len(text)
        ans = 0
        freq = Counter(text)

        for i in range(n):
            for j in range(i, n):
                ch = text[i]
                length = j - i + 1
                count = text[i:j + 1].count(ch)

                if length - count <= 1 and count <= freq[ch]:
                    ans = max(ans, min(length, freq[ch]))

        return ans
```

### Optimal — Corrected Python

python
```
from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        freq = Counter(text)
        n = len(text)
        ans = 0
        i = 0

        while i < n:
            j = i

            while j < n and text[j] == text[i]:
                j += 1

            left = j - i
            ans = max(ans, min(left + 1, freq[text[i]]))

            k = j + 1
            while k < n and text[k] == text[i]:
                k += 1

            right = k - j - 1

            if j < n:
                ans = max(
                    ans,
                    min(left + right + 1, freq[text[i]])
                )

            i = j

        return ans
```
