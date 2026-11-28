# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

# An integer y is a power of three if there exists an integer x such that y == 3x.



# Example 1:

# Input: n = 12
# Output: true
# Explanation: 12 = 31 + 32
# Example 2:

# Input: n = 91
# Output: true
# Explanation: 91 = 30 + 32 + 34
# Example 3:

# Input: n = 21
# Output: false


# Constraints:

# 1 <= n <= 107
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
# ### 1. Brute Force — Recursive (O(2^log₃n))

python

```python
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powers = []
        p = 1

        while p <= n:
            powers.append(p)
            p *= 3

        def solve(i, total):
            if total == n:
                return True
            if total > n or i == len(powers):
                return False

            return (solve(i + 1, total + powers[i]) or
                    solve(i + 1, total))

        return solve(0, 0)
```

### 2. Optimal — O(log₃ n)

python

```python
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 2:
                return False
            n //= 3

        return True
```
