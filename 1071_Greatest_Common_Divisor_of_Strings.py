# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"

# Output: "ABC"

# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"

# Output: "AB"

# Example 3:

# Input: str1 = "LEET", str2 = "CODE"

# Output: ""

# Example 4:

# Input: str1 = "AAAAAB", str2 = "AAA"

# Output: ""​​​​​​​



# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.
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
# ### Brute Force

python
```
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = min(len(str1), len(str2))

        for i in range(n, 0, -1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                x = str1[:i]

                if x * (len(str1) // i) == str1 and \
                   x * (len(str2) // i) == str2:
                    return x

        return ""
```

### Optimal (GCD)

python
```
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        return str1[:gcd(len(str1), len(str2))]
```
