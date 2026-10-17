# You are given a string text. You should split it to k substrings (subtext1, subtext2, ..., subtextk) such that:

# subtexti is a non-empty string.
# The concatenation of all the substrings is equal to text (i.e., subtext1 + subtext2 + ... + subtextk == text).
# subtexti == subtextk - i + 1 for all valid values of i (i.e., 1 <= i <= k).
# Return the largest possible value of k.



# Example 1:

# Input: text = "ghiabcdefhelloadamhelloabcdefghi"
# Output: 7
# Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
# Example 2:

# Input: text = "merchant"
# Output: 1
# Explanation: We can split the string on "(merchant)".
# Example 3:

# Input: text = "antaprezatepzapreanta"
# Output: 11
# Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)".


# Constraints:

# 1 <= text.length <= 1000
# text consists only of lowercase English characters.
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
# ### Brute Force — Python

python
```
class Solution:
    def longestDecomposition(self, text: str) -> int:
        count = 0

        while text:
            found = False

            for i in range(1, len(text) // 2 + 1):
                if text[:i] == text[-i:]:
                    count += 2
                    text = text[i:-i]
                    found = True
                    break

            if not found:
                count += 1
                break

        return count
```

### Optimal — Python

python
```
class Solution:
    def longestDecomposition(self, text: str) -> int:
        left = ""
        right = ""
        count = 0
        i, j = 0, len(text) - 1

        while i < j:
            left += text[i]
            right = text[j] + right

            if left == right:
                count += 2
                left = ""
                right = ""

            i += 1
            j -= 1

        if i == j or left or right:
            count += 1

        return count
```
