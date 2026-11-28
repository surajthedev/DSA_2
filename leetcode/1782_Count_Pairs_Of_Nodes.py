# You are given an undirected graph defined by an integer n, the number of nodes, and a 2D integer array edges, the edges in the graph, where edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi. You are also given an integer array queries.

# Let incident(a, b) be defined as the number of edges that are connected to either node a or b.

# The answer to the jth query is the number of pairs of nodes (a, b) that satisfy both of the following conditions:

# a < b
# incident(a, b) > queries[j]
# Return an array answers such that answers.length == queries.length and answers[j] is the answer of the jth query.

# Note that there can be multiple edges between the same two nodes.



# Example 1:


# Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
# Output: [6,5]
# Explanation: The calculations for incident(a, b) are shown in the table above.
# The answers for each of the queries are as follows:
# - answers[0] = 6. All the pairs have an incident(a, b) value greater than 2.
# - answers[1] = 5. All the pairs except (3, 4) have an incident(a, b) value greater than 3.
# Example 2:

# Input: n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
# Output: [10,10,9,8,6]


# Constraints:

# 2 <= n <= 2 * 104
# 1 <= edges.length <= 105
# 1 <= ui, vi <= n
# ui != vi
# 1 <= queries.length <= 20
# 0 <= queries[j] < edges.length
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
# ### 1. Brute Force — O(Q × N²)

python

```python
from collections import Counter

class Solution:
    def countPairs(self, n, edges, queries):
        degree = [0] * (n + 1)
        cnt = Counter()

        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            if u > v:
                u, v = v, u
            cnt[(u, v)] += 1

        ans = []

        for q in queries:
            total = 0

            for u in range(1, n + 1):
                for v in range(u + 1, n + 1):
                    incident = degree[u] + degree[v] - cnt[(u, v)]

                    if incident > q:
                        total += 1

            ans.append(total)

        return ans
```

### 2. Optimal — O(N² + E + Q × N log N)

python

```python
from collections import Counter

class Solution:
    def countPairs(self, n, edges, queries):
        degree = [0] * (n + 1)
        cnt = Counter()

        for u, v in edges:
            degree[u] += 1
            degree[v] += 1

            if u > v:
                u, v = v, u

            cnt[(u, v)] += 1

        arr = sorted(degree[1:])
        ans = []

        for q in queries:
            left, right = 0, n - 1
            total = 0

            while left < right:
                if arr[left] + arr[right] > q:
                    total += right - left
                    right -= 1
                else:
                    left += 1

            for (u, v), common in cnt.items():
                original = degree[u] + degree[v]
                adjusted = original - common

                if adjusted <= q < original:
                    total -= 1

            ans.append(total)

        return ans
```
