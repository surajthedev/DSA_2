# There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

# The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

# The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

# Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.



# Example 1:



# Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
# Output: 4
# Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.
# Example 2:



# Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
# Output: 5
# Explanation: There are 5 roads that are connected to cities 1 or 2.
# Example 3:

# Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
# Output: 5
# Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.


# Constraints:

# 2 <= n <= 100
# 0 <= roads.length <= n * (n - 1) / 2
# roads[i].length == 2
# 0 <= ai, bi <= n-1
# ai != bi
# Each pair of cities has at most one road connecting them.
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
# ### **1. Brute Force Solution**

```
class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        degree = [0] * n

        for u, v in roads:
            degree[u] += 1
            degree[v] += 1

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j]

                for u, v in roads:
                    if (u == i and v == j) or (u == j and v == i):
                        rank -= 1
                        break

                ans = max(ans, rank)

        return ans```

### **2. Optimal Solution (Degree + Adjacency Matrix)**

```
class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        degree = [0] * n
        connected = [[False] * n for _ in range(n)]

        for u, v in roads:
            degree[u] += 1
            degree[v] += 1

            connected[u][v] = True
            connected[v][u] = True

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j]

                if connected[i][j]:
                    rank -= 1

                ans = max(ans, rank)

        return ans```
