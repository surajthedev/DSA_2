# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

# Return all critical connections in the network in any order.



# Example 1:


# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
# Example 2:

# Input: n = 2, connections = [[0,1]]
# Output: [[0,1]]


# Constraints:

# 2 <= n <= 105
# n - 1 <= connections.length <= 105
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no repeated connections.
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
# ### Brute Force

python
```

from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        def is_connected(skip_u, skip_v):
            visited = set()
            stack = [0]
            visited.add(0)

            while stack:
                node = stack.pop()

                for nei in graph[node]:
                    if (node == skip_u and nei == skip_v) or (node == skip_v and nei == skip_u):
                        continue
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)

            return len(visited) == n

        result = []

        for u, v in connections:
            if not is_connected(u, v):
                result.append([u, v])

        return result
```

### Optimal — Tarjan's Algorithm

python
```

from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n
        low = [0] * n
        result = []
        timer = 0

        def dfs(node, parent):
            nonlocal timer

            disc[node] = low[node] = timer
            timer += 1

            for nei in graph[node]:
                if nei == parent:
                    continue

                if disc[nei] == -1:
                    dfs(nei, node)
                    low[node] = min(low[node], low[nei])

                    if low[nei] > disc[node]:
                        result.append([node, nei])
                else:
                    low[node] = min(low[node], disc[nei])

        dfs(0, -1)
        return result
```
