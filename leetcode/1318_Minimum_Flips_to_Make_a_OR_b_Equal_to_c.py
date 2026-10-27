# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.



# Example 1:



# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
# Example 2:

# Input: a = 4, b = 2, c = 7
# Output: 1
# Example 3:

# Input: a = 1, b = 2, c = 3
# Output: 0


# Constraints:

# 1 <= a <= 10^9
# 1 <= b <= 10^9
# 1 <= c <= 10^9
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
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0

        while a or b or c:
            x = a & 1
            y = b & 1
            z = c & 1

            if z == 0:
                ans += x + y
            else:
                if x == 0 and y == 0:
                    ans += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return ans
```

### Optimal

python

```
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0

        while a > 0 or b > 0 or c > 0:
            if (c & 1) == 0:
                ans += (a & 1) + (b & 1)
            elif (a & 1) == 0 and (b & 1) == 0:
                ans += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return ans
```
