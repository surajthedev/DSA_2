# Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

# It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

# Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.



# Example 1:

# Input: s = "?zs"
# Output: "azs"
# Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
# Example 2:

# Input: s = "ubv?w"
# Output: "ubvaw"
# Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".


# Constraints:

# 1 <= s.length <= 100
# s consist of lowercase English letters and '?'.
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
# ### **1. Brute Force — O(n × 26)**

```
class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)

        for i in range(len(s)):
            if s[i] == '?':
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if (i == 0 or s[i - 1] != ch) and \
                       (i == len(s) - 1 or s[i + 1] != ch):
                        s[i] = ch
                        break

        return ''.join(s)```

### **2. Optimal — O(n)**

```
class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)

        for i in range(len(s)):
            if s[i] == '?':
                for ch in 'abc':
                    if (i == 0 or s[i - 1] != ch) and \
                       (i == len(s) - 1 or s[i + 1] != ch):
                        s[i] = ch
                        break

        return ''.join(s)```
