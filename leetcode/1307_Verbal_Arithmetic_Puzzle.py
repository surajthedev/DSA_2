# Given an equation, represented by words on the left side and the result on the right side.

# You need to check if the equation is solvable under the following rules:

# Each character is decoded as one digit (0 - 9).
# No two characters can map to the same digit.
# Each words[i] and result are decoded as one number without leading zeros.
# Sum of numbers on the left side (words) will equal to the number on the right side (result).
# Return true if the equation is solvable, otherwise return false.



# Example 1:

# Input: words = ["SEND","MORE"], result = "MONEY"
# Output: true
# Explanation: Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
# Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
# Example 2:

# Input: words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
# Output: true
# Explanation: Map 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
# Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
# Example 3:

# Input: words = ["LEET","CODE"], result = "POINT"
# Output: false
# Explanation: There is no possible mapping to satisfy the equation, so we return false.
# Note that two different characters cannot map to the same digit.


# Constraints:

# 2 <= words.length <= 5
# 1 <= words[i].length, result.length <= 7
# words[i], result contain only uppercase English letters.
# The number of different characters used in the expression is at most 10.
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
from itertools import permutations

class Solution:
    def isSolvable(self, words: list[str], result: str) -> bool:
        chars = list(set("".join(words) + result))

        if len(chars) > 10:
            return False

        leading = {w[0] for w in words + [result] if len(w) > 1}

        for digits in permutations(range(10), len(chars)):
            mp = dict(zip(chars, digits))

            if any(mp[ch] == 0 for ch in leading):
                continue

            total = sum(
                sum(mp[ch] * (10 ** i) for i, ch in enumerate(w[::-1]))
                for w in words
            )

            target = sum(
                mp[ch] * (10 ** i)
                for i, ch in enumerate(result[::-1])
            )

            if total == target:
                return True

        return False
```

### Optimal (Column-wise Backtracking)

python

```
class Solution:
    def isSolvable(self, words: list[str], result: str) -> bool:
        if max(map(len, words)) > len(result):
            return False

        if sum(10 ** len(w) for w in words) < 10 ** (len(result) - 1):
            return False

        chars = set("".join(words) + result)
        if len(chars) > 10:
            return False

        leading = {w[0] for w in words + [result] if len(w) > 1}
        mapping = {}
        used = [False] * 10
        n = len(result)

        def dfs(col, idx, carry):
            if col == n:
                return carry == 0

            if idx < len(words):
                word = words[idx]

                if col >= len(word):
                    return dfs(col, idx + 1, carry)

                ch = word[-1 - col]

                if ch in mapping:
                    return dfs(col, idx + 1, carry + mapping[ch])

                for d in range(10):
                    if used[d] or (d == 0 and ch in leading):
                        continue

                    mapping[ch] = d
                    used[d] = True

                    if dfs(col, idx + 1, carry + d):
                        return True

                    del mapping[ch]
                    used[d] = False

                return False

            ch = result[-1 - col]
            digit = carry % 10
            new_carry = carry // 10

            if ch in mapping:
                if mapping[ch] != digit:
                    return False
                return dfs(col + 1, 0, new_carry)

            if used[digit] or (digit == 0 and ch in leading):
                return False

            mapping[ch] = digit
            used[digit] = True

            if dfs(col + 1, 0, new_carry):
                return True

            del mapping[ch]
            used[digit] = False
            return False

        return dfs(0, 0, 0)
```
