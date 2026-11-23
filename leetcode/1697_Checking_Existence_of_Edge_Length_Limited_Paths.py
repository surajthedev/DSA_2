# An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

# Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

# Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.



# Example 1:


# Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
# Output: [false,true]
# Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
# For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
# For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.
# Example 2:


# Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
# Output: [true,false]
# Explanation: The above figure shows the given graph.


# Constraints:

# 2 <= n <= 105
# 1 <= edgeList.length, queries.length <= 105
# edgeList[i].length == 3
# queries[j].length == 3
# 0 <= ui, vi, pj, qj <= n - 1
# ui != vi
# pj != qj
# 1 <= disi, limitj <= 109
# There may be multiple edges between two nodes.
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
# ### 1. Brute Force Approach (DFS)

python

```python

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]

        for u, v, w in edgeList:
            graph[u].append((v, w))
            graph[v].append((u, w))

        ans = []

        for src, dest, limit in queries:
            visited = set()
            stack = [src]
            found = False

            while stack:
                node = stack.pop()

                if node == dest:
                    found = True
                    break

                if node in visited:
                    continue

                visited.add(node)

                for nei, weight in graph[node]:
                    if weight < limit and nei not in visited:
                        stack.append(nei)

            ans.append(found)

        return ans
```

Time Complexity: O(Q × (V + E))

Space Complexity: O(V + E)

### 2. Optimal Approach (Sorting + Union Find / DSU)

Optimalpython

```python

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return

            if rank[rootX] < rank[rootY]:
                rootX, rootY = rootY, rootX

            parent[rootY] = rootX
            rank[rootX] += rank[rootY]

        edgeList.sort(key=lambda x: x[2])

        sorted_queries = sorted(
            [(limit, p, q, i) for i, (p, q, limit) in enumerate(queries)]
        )

        ans = [False] * len(queries)
        j = 0

        for limit, p, q, idx in sorted_queries:

            while j < len(edgeList) and edgeList[j][2] < limit:
                u, v, w = edgeList[j]
                union(u, v)
                j += 1

            ans[idx] = find(p) == find(q)

        return ans
```

Time Complexity: O((E + Q) log(E + Q) + (E + Q) α(V))

Space Complexity: O(V + Q)
