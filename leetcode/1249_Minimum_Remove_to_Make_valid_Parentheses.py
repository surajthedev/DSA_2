# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.


# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.


# Constraints:

# 1 <= s.length <= 105
# s[i] is either '(' , ')', or lowercase English letter.
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
    def minRemoveToMakeValid(self, s: str) -> str:
        from itertools import combinations

        indices = [i for i, ch in enumerate(s) if ch in "()"]

        for remove_count in range(len(indices) + 1):
            for removed in combinations(indices, remove_count):
                removed = set(removed)
                result = "".join(
                    ch for i, ch in enumerate(s) if i not in removed
                )

                balance = 0
                valid = True

                for ch in result:
                    if ch == '(':
                        balance += 1
                    elif ch == ')':
                        balance -= 1

                    if balance < 0:
                        valid = False
                        break

                if valid and balance == 0:
                    return result

        return ""
```

### Optimal — Stack

python
```
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        stack = []

        for i, ch in enumerate(chars):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    chars[i] = ''

        for i in stack:
            chars[i] = ''

        return ''.join(chars)
```
