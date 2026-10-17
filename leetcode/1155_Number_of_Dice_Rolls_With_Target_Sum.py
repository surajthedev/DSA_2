# You have n dice, and each dice has k faces numbered from 1 to k.

# Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.



# Example 1:

# Input: n = 1, k = 6, target = 3
# Output: 1
# Explanation: You throw one die with 6 faces.
# There is only one way to get a sum of 3.
# Example 2:

# Input: n = 2, k = 6, target = 7
# Output: 6
# Explanation: You throw two dice, each with 6 faces.
# There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
# Example 3:

# Input: n = 30, k = 30, target = 500
# Output: 222616187
# Explanation: The answer must be returned modulo 109 + 7.


# Constraints:

# 1 <= n, k <= 30
# 1 <= target <= 1000
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
# ### Brute Force — Python (Recursion + Memoization)

python
```
from functools import lru_cache

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def solve(dice, remaining):
            if dice == 0:
                return 1 if remaining == 0 else 0

            if remaining < dice or remaining > dice * k:
                return 0

            ways = 0
            for face in range(1, k + 1):
                ways += solve(dice - 1, remaining - face)

            return ways % MOD

        return solve(n, target)
```

### Optimal — Python (Dynamic Programming)

python
```
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1

        for dice in range(1, n + 1):
            new_dp = [0] * (target + 1)

            for total in range(dice, min(target, dice * k) + 1):
                for face in range(1, min(k, total) + 1):
                    new_dp[total] = (
                        new_dp[total] + dp[total - face]
                    ) % MOD

            dp = new_dp

        return dp[target]
```
