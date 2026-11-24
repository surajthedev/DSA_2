# You are given an array of positive integers nums.

# An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:

# prod(arr) is the product of all elements of arr.
# gcd(arr) is the GCD of all elements of arr.
# lcm(arr) is the LCM of all elements of arr.
# Return the length of the longest product equivalent subarray of nums.



# Example 1:

# Input: nums = [1,2,1,2,1,1,1]

# Output: 5

# Explanation:

# The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

# Example 2:

# Input: nums = [2,3,4,5,6]

# Output: 3

# Explanation:

# The longest product equivalent subarray is [3, 4, 5].

# Example 3:

# Input: nums = [1,2,3,1,4,5,1]

# Output: 5



# Constraints:

# 2 <= nums.length <= 100
# 1 <= nums[i] <= 10
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
# ### 1. Brute Force Approach

python

```python
from math import gcd, lcm
from functools import reduce

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        for i in range(n):
            prod = 1
            g = 0
            L = 1

            for j in range(i, n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                L = lcm(L, nums[j])

                if prod == g * L:
                    ans = max(ans, j - i + 1)

        return ans
```

### 2. Optimal Approach

python

```python
from math import gcd, lcm
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        for i in range(n):
            prod = 1
            g = 0
            L = 1

            for j in range(i, n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                L = lcm(L, nums[j])

                if prod == g * L:
                    ans = max(ans, j - i + 1)

        return ans
```
