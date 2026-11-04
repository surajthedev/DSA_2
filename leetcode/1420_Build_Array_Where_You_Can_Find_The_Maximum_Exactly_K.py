# You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:


# You should build the array arr which has the following properties:

# arr has exactly n integers.
# 1 <= arr[i] <= m where (0 <= i < n).
# After applying the mentioned algorithm to arr, the value search_cost is equal to k.
# Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.



# Example 1:

# Input: n = 2, m = 3, k = 1
# Output: 6
# Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
# Example 2:

# Input: n = 5, m = 2, k = 3
# Output: 0
# Explanation: There are no possible arrays that satisfy the mentioned conditions.
# Example 3:

# Input: n = 9, m = 1, k = 1
# Output: 1
# Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]


# Constraints:

# 1 <= n <= 50
# 1 <= m <= 100
# 0 <= k <= n
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
# ### 1. Brute Force Approach (Recursive + Memoization)

python

```python
from functools import lru_cache
from typing import List

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def solve(index, maximum, cost):
            if index == n:
                return 1 if cost == k else 0

            ans = 0

            for num in range(1, m + 1):
                if num > maximum:
                    ans += solve(index + 1, num, cost + 1)
                else:
                    ans += solve(index + 1, maximum, cost)

            return ans % MOD

        return solve(0, 0, 0)
```

Time Complexity: $O(n \times m \times k \times m)$

Space Complexity: $O(n \times m \times k)$

### 2. Optimal Approach (Dynamic Programming + Prefix Sum)

python

```python
from typing import List

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        for j in range(1, m + 1):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for max_val in range(1, m + 1):
                for cost in range(1, k + 1):
                    # Add a number <= current maximum
                    dp[i][max_val][cost] = (
                        dp[i - 1][max_val][cost] * max_val
                    ) % MOD

                    # Add a new maximum
                    for prev_max in range(1, max_val):
                        dp[i][max_val][cost] += dp[i - 1][prev_max][cost - 1]

                    dp[i][max_val][cost] %= MOD

        return sum(dp[n][j][k] for j in range(1, m + 1)) % MOD
```

Time Complexity: $O(n \times m^2 \times k)$

Space Complexity: $O(n \times m \times k)$
