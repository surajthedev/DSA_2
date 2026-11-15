# Alice and Bob have an undirected graph of n nodes and three types of edges:

# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can be traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

# Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.



# Example 1:



# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
# Example 2:



# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# Output: 0
# Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
# Example 3:



# Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# Output: -1
# Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.




# Constraints:

# 1 <= n <= 105
# 1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
# edges[i].length == 3
# 1 <= typei <= 3
# 1 <= ui < vi <= n
# All tuples (typei, ui, vi) are distinct.
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
# ### **1. Brute Force — Not Efficient (Repeated DFS)**

```
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def isConnected(edge_list):
            graph = [[] for _ in range(n + 1)]

            for u, v in edge_list:
                graph[u].append(v)
                graph[v].append(u)

            visited = set()
            stack = [1]

            while stack:
                node = stack.pop()

                if node in visited:
                    continue

                visited.add(node)

                for nei in graph[node]:
                    if nei not in visited:
                        stack.append(nei)

            return len(visited) == n

        removable = 0

        for i in range(len(edges)):
            temp = edges[:i] + edges[i + 1:]

            alice = []
            bob = []

            for t, u, v in temp:
                if t == 3 or t == 1:
                    alice.append((u, v))
                if t == 3 or t == 2:
                    bob.append((u, v))

            if isConnected(alice) and isConnected(bob):
                removable += 1

        return -1```

### **2. Optimal — O(E × α(n))**

```
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px

        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        self.components -= 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = DSU(n)
        bob = DSU(n)

        used = 0

        for t, u, v in edges:
            if t == 3:
                a = alice.union(u, v)
                b = bob.union(u, v)

                if a or b:
                    used += 1

        for t, u, v in edges:
            if t == 1:
                if alice.union(u, v):
                    used += 1

            elif t == 2:
                if bob.union(u, v):
                    used += 1

        if alice.components > 1 or bob.components > 1:
            return -1

        return len(edges) - used```
