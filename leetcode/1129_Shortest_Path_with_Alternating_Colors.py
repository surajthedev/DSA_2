# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

# You are given two arrays redEdges and blueEdges where:

# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.



# Example 1:

# Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
# Output: [0,1,-1]
# Example 2:

# Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
# Output: [0,1,-1]


# Constraints:

# 1 <= n <= 100
# 0 <= redEdges.length, blueEdges.length <= 400
# redEdges[i].length == blueEdges[j].length == 2
# 0 <= ai, bi, uj, vj < n
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
# ### Brute Force — BFS

python
```
from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[[] for _ in range(2)] for _ in range(n)]

        for u, v in redEdges:
            graph[u][0].append(v)

        for u, v in blueEdges:
            graph[u][1].append(v)

        ans = [-1] * n
        queue = deque([(0, 0, 0), (0, 1, 0)])
        visited = set()

        while queue:
            node, color, dist = queue.popleft()

            if (node, color) in visited:
                continue

            visited.add((node, color))

            if ans[node] == -1:
                ans[node] = dist

            for nei in graph[node][1 - color]:
                queue.append((nei, 1 - color, dist + 1))

        return ans
```

### Optimal — BFS with Visited States

python
```
from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[[] for _ in range(2)] for _ in range(n)]

        for u, v in redEdges:
            graph[u][0].append(v)

        for u, v in blueEdges:
            graph[u][1].append(v)

        dist = [[-1, -1] for _ in range(n)]
        dist[0] = [0, 0]

        queue = deque([(0, 0), (0, 1)])

        while queue:
            node, last_color = queue.popleft()

            next_color = 1 - last_color

            for nei in graph[node][next_color]:
                if dist[nei][next_color] == -1:
                    dist[nei][next_color] = dist[node][last_color] + 1
                    queue.append((nei, next_color))

        ans = []

        for red_dist, blue_dist in dist:
            valid = [d for d in (red_dist, blue_dist) if d != -1]
            ans.append(min(valid) if valid else -1)

        return ans
```
