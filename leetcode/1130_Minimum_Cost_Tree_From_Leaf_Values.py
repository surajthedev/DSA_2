# Given an array arr of positive integers, consider all binary trees such that:

# Each node has either 0 or 2 children;
# The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
# The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
# Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

# A node is a leaf if and only if it has zero children.



# Example 1:


# Input: arr = [6,2,4]
# Output: 32
# Explanation: There are two possible trees shown.
# The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.
# Example 2:


# Input: arr = [4,11]
# Output: 44


# Constraints:

# 2 <= arr.length <= 40
# 1 <= arr[i] <= 15
# It is guaranteed that the answer fits into a 32-bit signed integer (i.e., it is less than 231).
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
# ## Brute Force — O(n × 2ⁿ) approx. (Recursive)

python
```
from typing import List
from functools import lru_cache

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)

        @lru_cache(None)
        def solve(i, j):
            if i == j:
                return 0, arr[i]

            ans = float('inf')
            max_val = 0

            for k in range(i, j):
                left_cost, left_max = solve(i, k)
                right_cost, right_max = solve(k + 1, j)

                cost = left_cost + right_cost + left_max * right_max
                ans = min(ans, cost)
                max_val = max(max_val, left_max, right_max)

            return ans, max_val

        return solve(0, n - 1)[0]
```

## Optimal — O(n) (Monotonic Stack)

python
```
from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        ans = 0

        for x in arr:
            while stack[-1] <= x:
                mid = stack.pop()
                ans += mid * min(stack[-1], x)
            stack.append(x)

        while len(stack) > 2:
            ans += stack.pop() * stack[-1]

        return ans
```
