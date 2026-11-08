# There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer should not be painted again.

# A neighborhood is a maximal group of continuous houses that are painted with the same color.

# For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
# Given an array houses, an m x n matrix cost and an integer target where:

# houses[i]: is the color of the house i, and 0 if the house is not painted yet.
# cost[i][j]: is the cost of paint the house i with the color j + 1.
# Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.



# Example 1:

# Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
# Output: 9
# Explanation: Paint houses of this way [1,2,2,1,1]
# This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
# Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
# Example 2:

# Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
# Output: 11
# Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
# This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}].
# Cost of paint the first and last house (10 + 1) = 11.
# Example 3:

# Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
# Output: -1
# Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.


# Constraints:

# m == houses.length == cost.length
# n == cost[i].length
# 1 <= m <= 100
# 1 <= n <= 20
# 1 <= target <= m
# 0 <= houses[i] <= n
# 1 <= cost[i][j] <= 104
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
# ### 1. Brute Force Approach (Recursion + Memoization)

python

```python
from functools import lru_cache
from typing import List

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def dp(i, prev, neighborhoods):
            if neighborhoods > target:
                return float('inf')

            if i == m:
                return 0 if neighborhoods == target else float('inf')

            ans = float('inf')

            if houses[i] != 0:
                new_neighborhoods = neighborhoods + (houses[i] != prev)

                ans = dp(i + 1, houses[i], new_neighborhoods)

            else:
                for color in range(1, n + 1):
                    new_neighborhoods = neighborhoods + (color != prev)

                    paint_cost = cost[i][color - 1]

                    ans = min(
                        ans,
                        paint_cost + dp(i + 1, color, new_neighborhoods)
                    )

            return ans

        result = dp(0, 0, 0)

        return -1 if result == float('inf') else result
```

Time Complexity: O(m × n × target)

Space Complexity: O(m × n × target)

### 2. Optimal Approach (Dynamic Programming)

python

```python
from typing import List

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        INF = float('inf')

        dp = [[[INF] * (target + 1) for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0][0] = 0

        for i in range(1, m + 1):
            for color in range(1, n + 1):

                if houses[i - 1] != 0 and houses[i - 1] != color:
                    continue

                paint_cost = 0 if houses[i - 1] != 0 else cost[i - 1][color - 1]

                for prev in range(n + 1):
                    for neighborhoods in range(1, target + 1):

                        new_neighborhoods = neighborhoods

                        if prev != color:
                            new_neighborhoods = neighborhoods - 1

                        if new_neighborhoods < 0:
                            continue

                        dp[i][color][neighborhoods] = min(
                            dp[i][color][neighborhoods],
                            dp[i - 1][prev][new_neighborhoods] + paint_cost
                        )

        ans = min(dp[m][color][target] for color in range(1, n + 1))

        return -1 if ans == INF else ans
```

Time Complexity: O(m × n² × target)

Space Complexity: O(m × n × target)
