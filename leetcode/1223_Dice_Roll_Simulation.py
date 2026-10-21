# A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times.

# Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls. Since the answer may be too large, return it modulo 109 + 7.

# Two sequences are considered different if at least one element differs from each other.



# Example 1:

# Input: n = 2, rollMax = [1,1,2,2,2,3]
# Output: 34
# Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.
# Example 2:

# Input: n = 2, rollMax = [1,1,1,1,1,1]
# Output: 30
# Example 3:

# Input: n = 3, rollMax = [1,1,1,2,2,3]
# Output: 181


# Constraints:

# 1 <= n <= 5000
# rollMax.length == 6
# 1 <= rollMax[i] <= 15
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
### Brute Force (Recursion + Memoization)

python
```
from functools import lru_cache
from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(pos, last, count):
            if pos == n:
                return 1

            ans = 0
            for face in range(6):
                if face == last:
                    if count < rollMax[face]:
                        ans += dfs(pos + 1, face, count + 1)
                else:
                    ans += dfs(pos + 1, face, 1)

            return ans % MOD

        return dfs(0, -1, 0)
```

### Optimal Solution — Dynamic Programming

python
```
from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7

        dp = [[0] * 6 for _ in range(n + 1)]
        total = [0] * (n + 1)

        total[0] = 1

        for i in range(1, n + 1):
            for face in range(6):
                ways = total[i - 1]

                if i - rollMax[face] - 1 >= 0:
                    ways -= total[i - rollMax[face] - 1]
                    ways += dp[i - rollMax[face] - 1][face]

                dp[i][face] = ways % MOD
                total[i] = (total[i] + dp[i][face]) % MOD

        return total[n]
```
