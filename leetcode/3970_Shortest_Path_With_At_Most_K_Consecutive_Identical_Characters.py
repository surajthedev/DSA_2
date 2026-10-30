# You are given an integer n representing the number of nodes in a directed weighted graph, numbered from 0 to n - 1. This is represented by a 2D integer array edges, where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with weight wi.

# You are also given a string labels of length n, where labels[i] is the character assigned to node i, and an integer k.

# Return the minimum total edge weight of a path from node 0 to node n - 1 such that the concatenation of the labels of the nodes along the path contains at most k consecutive identical characters. If no valid path exists, return -1.



# Example 1:

# Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1

# Output: 3

# Explanation:

# The optimal valid path from node 0 to node 2 is as follows:

# Use edges[2] = [0, 2, 3] to reach node 2 with a weight wi = 3.
# The corresponding concatenation of labels is "ab", which satisfies at most k = 1 consecutive identical characters. Thus, the answer is 3.
# Example 2:

# Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2

# Output: 2

# Explanation:

# The optimal valid path from node 0 to node 2 is as follows:

# Use edges[0] = [0, 1, 1] to reach node 1 with weight wi = 1.
# Use edges[1] = [1, 2, 1] to reach node 2 with weight wi = 1.
# The corresponding concatenation of labels is "aab", which satisfies at most k = 2 consecutive identical characters. Thus, the answer is 2.
# Example 3:

# Input: n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2

# Output: -1

# Explanation:

# There is no valid path from node 0 to node 2 that satisfies at most k = 2 consecutive identical characters. Thus, the answer is -1.



# Constraints:

# 1 <= n == labels.length <= 5 * 104
# 0 <= edges.length <= 5 * 104
# edges[i] == [ui, vi, wi]
# 0 <= ui, vi <= n - 1
# ui != vi
# 1 <= wi <= 104
# labels consists of lowercase English letters
# 1 <= k <= 50
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
# ### 1. Brute Force (DFS + Memoization)

python

```
from functools import lru_cache
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))

        INF = float('inf')

        @lru_cache(None)
        def dfs(node, prev_char, count):
            if node == n - 1:
                return 0

            ans = INF

            for nei, weight in graph[node]:
                ch = labels[nei]

                new_count = count + 1 if ch == prev_char else 1

                if new_count <= k:
                    cost = dfs(nei, ch, new_count)

                    if cost != INF:
                        ans = min(ans, weight + cost)

            return ans

        result = dfs(0, labels[0], 1)

        return result if result != INF else -1
```

### 2. Optimal (Dijkstra + State)

python

```
import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))

        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        dist[0][1] = 0
        pq = [(0, 0, 1)]

        while pq:
            cost, node, count = heapq.heappop(pq)

            if cost != dist[node][count]:
                continue

            if node == n - 1:
                return cost

            for nei, weight in graph[node]:
                if labels[nei] == labels[node]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[nei][new_count]:
                    dist[nei][new_count] = new_cost
                    heapq.heappush(
                        pq, (new_cost, nei, new_count)
                    )

        return -1
