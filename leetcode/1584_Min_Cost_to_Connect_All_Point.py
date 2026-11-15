# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.



# Example 1:


# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation:

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# Example 2:

# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18


# Constraints:

# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# All pairs (xi, yi) are distinct.
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
#
#
#
#
# ### **1. Brute Force — O(n³)**

```
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = {0}
        total = 0

        while len(visited) < n:
            min_cost = float('inf')
            next_point = -1

            for i in visited:
                for j in range(n):
                    if j not in visited:
                        cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                        if cost < min_cost:
                            min_cost = cost
                            next_point = j

            total += min_cost
            visited.add(next_point)

        return total```

### **2. Optimal — Prim's Algorithm — O(n²)**

```
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        min_dist = [float('inf')] * n

        min_dist[0] = 0
        total = 0

        for _ in range(n):
            u = -1

            for i in range(n):
                if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i

            visited[u] = True
            total += min_dist[u]

            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    min_dist[v] = min(min_dist[v], dist)

        return total```
