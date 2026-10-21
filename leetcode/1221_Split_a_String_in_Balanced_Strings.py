# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it into some number of substrings such that:

# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.



# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
# Example 2:

# Input: s = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
# Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.
# Example 3:

# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".


# Constraints:

# 2 <= s.length <= 1000
# s[i] is either 'L' or 'R'.
# s is a balanced string.
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
# ### Brute Force

python
```
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            l = 0
            r = 0

            for j in range(i, len(s)):
                if s[j] == 'L':
                    l += 1
                else:
                    r += 1

                if l == r:
                    ans += 1
                    i = j
                    break

        return ans
```

### Optimal Solution — O(n)

python
```
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        ans = 0

        for ch in s:
            if ch == 'L':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                ans += 1

        return ans
```
