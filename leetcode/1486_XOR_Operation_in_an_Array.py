# You are given an integer n and an integer start.

# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

# Return the bitwise XOR of all elements of nums.



# Example 1:

# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
# Where "^" corresponds to bitwise XOR operator.
# Example 2:

# Input: n = 4, start = 3
# Output: 8
# Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.


# Constraints:

# 1 <= n <= 1000
# 0 <= start <= 1000
# n == nums.length
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
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0

        for i in range(n):
            ans ^= start + 2 * i

        return ans
```

Time Complexity: O(n)

Space Complexity: O(1)

### 2. Optimal Approach (Mathematical + XOR)

python

```python
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        def xor_upto(x):
            if x % 4 == 0:
                return x
            elif x % 4 == 1:
                return 1
            elif x % 4 == 2:
                return x + 1
            else:
                return 0

        s = start // 2
        return (xor_upto(s + n - 1) ^ xor_upto(s - 1)) * 2 + (n % 2) * (start % 2)
```

Time Complexity: O(1)

Space Complexity: O(1)
