# You are given an undirected graph. You are given an integer n which is the number of nodes in the graph and an array edges, where each edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi.

# A connected trio is a set of three nodes where there is an edge between every pair of them.

# The degree of a connected trio is the number of edges where one endpoint is in the trio, and the other is not.

# Return the minimum degree of a connected trio in the graph, or -1 if the graph has no connected trios.



# Example 1:


# Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
# Output: 3
# Explanation: There is exactly one trio, which is [1,2,3]. The edges that form its degree are bolded in the figure above.
# Example 2:


# Input: n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
# Output: 0
# Explanation: There are exactly three trios:
# 1) [1,4,3] with degree 0.
# 2) [2,5,6] with degree 2.
# 3) [5,6,7] with degree 2.


# Constraints:

# 2 <= n <= 400
# edges[i].length == 2
# 1 <= edges.length <= n * (n-1) / 2
# 1 <= ui, vi <= n
# ui != vi
# There are no repeated edges.
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
#
#
#
#
# ### 1. Brute Force Approach

Time Complexity: $O(n^3)$

python

```python
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = [[False] * (n + 1) for _ in range(n + 1)]
        degree = [0] * (n + 1)

        for u, v in edges:
            graph[u][v] = True
            graph[v][u] = True
            degree[u] += 1
            degree[v] += 1

        ans = float('inf')

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if not graph[i][j]:
                    continue

                for k in range(j + 1, n + 1):
                    if graph[i][k] and graph[j][k]:
                        trio_degree = degree[i] + degree[j] + degree[k] - 6
                        ans = min(ans, trio_degree)

        return ans if ans != float('inf') else -1
```

### 2. Optimal Approach (Degree-Based Optimization)

O(n² + E)python

```python
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = [set() for _ in range(n + 1)]
        degree = [0] * (n + 1)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degree[u] += 1
            degree[v] += 1

        ans = float('inf')

        for u in range(1, n + 1):
            for v in graph[u]:
                if v <= u:
                    continue

                for w in graph[v]:
                    if w <= v:
                        continue

                    if w in graph[u]:
                        ans = min(
                            ans,
                            degree[u] + degree[v] + degree[w] - 6
                        )

        return ans if ans != float('inf') else -1
```
