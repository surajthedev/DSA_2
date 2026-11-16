# You are given two groups of points where the first group has size1 points, the second group has size2 points, and size1 >= size2.

# The cost of the connection between any two points are given in an size1 x size2 matrix where cost[i][j] is the cost of connecting point i of the first group and point j of the second group. The groups are connected if each point in both groups is connected to one or more points in the opposite group. In other words, each point in the first group must be connected to at least one point in the second group, and each point in the second group must be connected to at least one point in the first group.

# Return the minimum cost it takes to connect the two groups.



# Example 1:


# Input: cost = [[15, 96], [36, 2]]
# Output: 17
# Explanation: The optimal way of connecting the groups is:
# 1--A
# 2--B
# This results in a total cost of 17.
# Example 2:


# Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
# Output: 4
# Explanation: The optimal way of connecting the groups is:
# 1--A
# 2--B
# 2--C
# 3--A
# This results in a total cost of 4.
# Note that there are multiple points connected to point 2 in the first group and point A in the second group. This does not matter as there is no limit to the number of points that can be connected. We only care about the minimum total cost.
# Example 3:

# Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
# Output: 10


# Constraints:

# size1 == cost.length
# size2 == cost[i].length
# 1 <= size1, size2 <= 12
# size1 >= size2
# 0 <= cost[i][j] <= 100
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
# **Brute Force — Bitmask DP (O(size1 × 2^size2 × size2))**

```
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        INF = float('inf')

        dp = [[INF] * (1 << n) for _ in range(m + 1)]
        dp[0][0] = 0

        for i in range(m):
            for mask in range(1 << n):
                if dp[i][mask] == INF:
                    continue

                for j in range(n):
                    new_mask = mask | (1 << j)
                    dp[i + 1][new_mask] = min(
                        dp[i + 1][new_mask],
                        dp[i][mask] + cost[i][j]
                    )

        return min(
            dp[m][mask] + sum(
                min(cost[i][j] for i in range(m))
                for j in range(n)
                if not (mask & (1 << j))
            )
            for mask in range(1 << n)
        )```

**Optimal — Bitmask DP (O(size1 × size2 × 2^size2))**

```
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        INF = float('inf')

        min_cost = [
            min(cost[i][j] for i in range(m))
            for j in range(n)
        ]

        dp = [INF] * (1 << n)
        dp[0] = 0

        for i in range(m):
            new_dp = [INF] * (1 << n)

            for mask in range(1 << n):
                if dp[mask] == INF:
                    continue

                for j in range(n):
                    new_mask = mask | (1 << j)

                    new_dp[new_mask] = min(
                        new_dp[new_mask],
                        dp[mask] + cost[i][j]
                    )

            dp = new_dp

        ans = INF

        for mask in range(1 << n):
            total = dp[mask]

            for j in range(n):
                if not (mask & (1 << j)):
                    total += min_cost[j]

            ans = min(ans, total)

        return ans```
