# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.

# The test cases are generated so that a unique mapping will always exist.



# Example 1:

# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
# Example 2:

# Input: s = "1326#"
# Output: "acz"


# Constraints:

# 1 <= s.length <= 1000
# s consists of digits and the '#' letter.
# s will be a valid string such that mapping is always possible.
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
# ### 1. Brute Force

python

```
class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = 0

        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                num = int(s[i:i + 2])
                result.append(chr(ord('a') + num - 1))
                i += 3
            else:
                num = int(s[i])
                result.append(chr(ord('a') + num - 1))
                i += 1

        return ''.join(result)
```

### 2. Optimal (Right to Left)

python

```
class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = len(s) - 1

        while i >= 0:
            if s[i] == '#':
                num = int(s[i - 2:i])
                result.append(chr(ord('a') + num - 1))
                i -= 3
            else:
                result.append(chr(ord('a') + int(s[i]) - 1))
                i -= 1

        return ''.join(result[::-1])
```
