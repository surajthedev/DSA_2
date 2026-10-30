# Given an array of digits digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order. If there is no answer return an empty string.

# Since the answer may not fit in an integer data type, return the answer as a string. Note that the returning answer must not contain unnecessary leading zeros.



# Example 1:

# Input: digits = [8,1,9]
# Output: "981"
# Example 2:

# Input: digits = [8,6,7,1,0]
# Output: "8760"
# Example 3:

# Input: digits = [1]
# Output: ""


# Constraints:

# 1 <= digits.length <= 104
# 0 <= digits[i] <= 9
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
# ### Brute Force Solution

python

```
from itertools import combinations

class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        digits.sort(reverse=True)
        n = len(digits)
        ans = ""

        for mask in range(1, 1 << n):
            arr = [digits[i] for i in range(n) if mask & (1 << i)]

            if sum(arr) % 3 == 0:
                arr.sort(reverse=True)
                s = ''.join(map(str, arr))

                if s[0] == '0':
                    s = '0'

                if len(s) > len(ans) or (len(s) == len(ans) and s > ans):
                    ans = s

        return ans
```

Time Complexity: $O(2^n \cdot n)$

### Optimal Solution (Greedy)

python

```
class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        digits.sort(reverse=True)

        remainder = sum(digits) % 3

        if remainder == 1:
            for i in range(len(digits)):
                if digits[i] % 3 == 1:
                    digits.pop(i)
                    break
            else:
                count = 0
                i = 0

                while i < len(digits) and count < 2:
                    if digits[i] % 3 == 2:
                        digits.pop(i)
                        count += 1
                    else:
                        i += 1

        elif remainder == 2:
            for i in range(len(digits)):
                if digits[i] % 3 == 2:
                    digits.pop(i)
                    break
            else:
                count = 0
                i = 0

                while i < len(digits) and count < 2:
                    if digits[i] % 3 == 1:
                        digits.pop(i)
                        count += 1
                    else:
                        i += 1

        if not digits:
            return ""

        if digits[0] == 0:
            return "0"

        return ''.join(map(str, digits))
```
