# Given the array houses where houses[i] is the location of the ith house along a street and an integer k, allocate k mailboxes in the street.

# Return the minimum total distance between each house and its nearest mailbox.

# The test cases are generated so that the answer fits in a 32-bit integer.



# Example 1:


# Input: houses = [1,4,8,10,20], k = 3
# Output: 5
# Explanation: Allocate mailboxes in position 3, 9 and 20.
# Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5
# Example 2:


# Input: houses = [2,3,5,12,18], k = 2
# Output: 9
# Explanation: Allocate mailboxes in position 3 and 14.
# Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.


# Constraints:

# 1 <= k <= houses.length <= 100
# 1 <= houses[i] <= 104
# All the integers of houses are unique.
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
# ### 1. Brute Force Approach (DP + Median)

python

```python
from typing import List
from functools import lru_cache

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        def cost(i, j):
            mid = (i + j) // 2
            return sum(abs(houses[x] - houses[mid]) for x in range(i, j + 1))

        @lru_cache(None)
        def dp(i, boxes):
            if i == n:
                return 0 if boxes == 0 else float('inf')

            if boxes == 0:
                return float('inf')

            ans = float('inf')

            for j in range(i, n):
                ans = min(ans, cost(i, j) + dp(j + 1, boxes - 1))

            return ans

        return dp(0, k)
```

Time Complexity: O(k × n³)

Space Complexity: O(k × n)

### 2. Optimal Approach (Precomputed Cost + DP)

python

```python
from typing import List

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)

        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                mid = (i + j) // 2
                cost[i][j] = sum(
                    abs(houses[x] - houses[mid])
                    for x in range(i, j + 1)
                )

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for boxes in range(1, min(i, k) + 1):
                for j in range(boxes - 1, i):
                    dp[i][boxes] = min(
                        dp[i][boxes],
                        dp[j][boxes - 1] + cost[j][i - 1]
                    )

        return dp[n][k]
```

Time Complexity: O(n³ + k × n²)

Space Complexity: O(n² + k × n)
