# You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

# In the ith operation (1-indexed), you will:

# Choose two elements, x and y.
# Receive a score of i * gcd(x, y).
# Remove x and y from nums.
# Return the maximum score you can receive after performing n operations.

# The function gcd(x, y) is the greatest common divisor of x and y.



# Example 1:

# Input: nums = [1,2]
# Output: 1
# Explanation: The optimal choice of operations is:
# (1 * gcd(1, 2)) = 1
# Example 2:

# Input: nums = [3,4,6,8]
# Output: 11
# Explanation: The optimal choice of operations is:
# (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
# Example 3:

# Input: nums = [1,2,3,4,5,6]
# Output: 14
# Explanation: The optimal choice of operations is:
# (1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14


# Constraints:

# 1 <= n <= 7
# nums.length == 2 * n
# 1 <= nums[i] <= 106
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
# ### Brute Force (Backtracking)

python

```python

from math import gcd

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        def backtrack(mask, op):
            if mask == (1 << n) - 1:
                return 0

            ans = 0

            for i in range(n):
                if mask & (1 << i):
                    continue

                for j in range(i + 1, n):
                    if mask & (1 << j):
                        continue

                    score = op * gcd(nums[i], nums[j])
                    new_mask = mask | (1 << i) | (1 << j)

                    ans = max(ans, score + backtrack(new_mask, op + 1))

            return ans

        return backtrack(0, 1)
```

### Optimal (Bitmask DP + Memoization)

Optimalpython

```python

from math import gcd
from functools import lru_cache
from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        full_mask = (1 << n) - 1

        @lru_cache(None)
        def dp(mask):
            if mask == full_mask:
                return 0

            op = mask.bit_count() // 2 + 1
            ans = 0

            for i in range(n):
                if mask & (1 << i):
                    continue

                for j in range(i + 1, n):
                    if mask & (1 << j):
                        continue

                    new_mask = mask | (1 << i) | (1 << j)

                    score = op * gcd(nums[i], nums[j])
                    ans = max(ans, score + dp(new_mask))

            return ans

        return dp(0)
```
