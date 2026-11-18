# There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.

# A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.

# For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.

# Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.

# Notice that the distance between the two cities is the number of edges in the path between them.



# Example 1:



# Input: n = 4, edges = [[1,2],[2,3],[2,4]]
# Output: [3,4,0]
# Explanation:
# The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
# The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
# No subtree has two nodes where the max distance between them is 3.
# Example 2:

# Input: n = 2, edges = [[1,2]]
# Output: [1]
# Example 3:

# Input: n = 3, edges = [[1,2],[2,3]]
# Output: [2,1]


# Constraints:

# 2 <= n <= 15
# edges.length == n-1
# edges[i].length == 2
# 1 <= ui, vi <= n
# All pairs (ui, vi) are distinct.
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

python

```python
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[0] * n for _ in range(n)]

        for u, v in edges:
            graph[u - 1][v - 1] = 1
            graph[v - 1][u - 1] = 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if graph[i][k] and graph[k][j]:
                        graph[i][j] = min(
                            graph[i][j] or float('inf'),
                            graph[i][k] + graph[k][j]
                        )

        ans = [0] * (n - 1)

        for mask in range(1, 1 << n):
            nodes = [i for i in range(n) if mask & (1 << i)]

            if len(nodes) < 2:
                continue

            connected = True

            for i in nodes:
                for j in nodes:
                    if graph[i][j] == 0 and i != j:
                        connected = False
                        break
                if not connected:
                    break

            if not connected:
                continue

            diameter = max(
                graph[i][j]
                for i in nodes
                for j in nodes
            )

            ans[diameter - 1] += 1

        return ans
```

### 2. Optimal Approach (Bitmask + DFS)

python

```python
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        dist = [[0] * n for _ in range(n)]

        for start in range(n):
            stack = [(start, -1, 0)]

            while stack:
                node, parent, d = stack.pop()
                dist[start][node] = d

                for nei in graph[node]:
                    if nei != parent:
                        stack.append((nei, node, d + 1))

        ans = [0] * (n - 1)

        for mask in range(1 << n):
            if mask.bit_count() < 2:
                continue

            nodes = [i for i in range(n) if mask & (1 << i)]

            visited = {nodes[0]}
            stack = [nodes[0]]

            while stack:
                node = stack.pop()

                for nei in graph[node]:
                    if (mask & (1 << nei)) and nei not in visited:
                        visited.add(nei)
                        stack.append(nei)

            if len(visited) != len(nodes):
                continue

            diameter = 0

            for i in nodes:
                for j in nodes:
                    diameter = max(diameter, dist[i][j])

            ans[diameter - 1] += 1

        return ans
```
