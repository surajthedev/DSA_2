# Given two positive integers n and k, the binary string Sn is formed as follows:

# S1 = "0"
# Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
# Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

# For example, the first four strings in the above sequence are:

# S1 = "0"
# S2 = "011"
# S3 = "0111001"
# S4 = "011100110110001"
# Return the kth bit in Sn. It is guaranteed that k is valid for the given n.



# Example 1:

# Input: n = 3, k = 1
# Output: "0"
# Explanation: S3 is "0111001".
# The 1st bit is "0".
# Example 2:

# Input: n = 4, k = 11
# Output: "1"
# Explanation: S4 is "011100110110001".
# The 11th bit is "1".


# Constraints:

# 1 <= n <= 20
# 1 <= k <= 2n - 1
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
# ### 1. Brute Force – O(2ⁿ)

python

```python
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"

        for _ in range(n - 1):
            inverted = ''.join('1' if ch == '0' else '0' for ch in s[::-1])
            s = s + "1" + inverted

        return s[k - 1]
```

### 2. Optimal – Recursion – O(n)

python

```python
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        invert = False

        while n > 1:
            mid = 1 << (n - 1)

            if k == mid:
                return "1" if not invert else "0"

            if k > mid:
                k = (1 << n) - k
                invert = not invert

            n -= 1

        return "1" if invert else "0"
```
