# There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

# Return a sorted list of the items such that:

# The items that belong to the same group are next to each other in the sorted list.
# There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
# Return any solution if there is more than one solution and return an empty list if there is no solution.



# Example 1:



# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
# Output: [6,3,4,1,5,2,0,7]
# Example 2:

# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
# Output: []
# Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.


# Constraints:

# 1 <= m <= n <= 3 * 104
# group.length == beforeItems.length == n
# -1 <= group[i] <= m - 1
# 0 <= beforeItems[i].length <= n - 1
# 0 <= beforeItems[i][j] <= n - 1
# i != beforeItems[i][j]
# beforeItems[i] does not contain duplicates elements.
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
# ### Brute Force

python
```
from collections import deque

class Solution:
    def sortItems(self, n, m, group, beforeItems):
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for i in range(n):
            for j in beforeItems[i]:
                adj[j].append(i)
                indegree[i] += 1

        q = deque(i for i in range(n) if indegree[i] == 0)
        order = []

        while q:
            u = q.popleft()
            order.append(u)

            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        if len(order) != n:
            return []

        result = []
        used = set()

        for g in range(m):
            items = [i for i in order if group[i] == g]
            if items:
                result.extend(items)
                used.add(g)

        return result if len(result) == n else []
```

### Optimal — Topological Sort (Group + Item Graph)

python
```
from collections import deque, defaultdict

class Solution:
    def sortItems(self, n, m, group, beforeItems):
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n

        group_graph = [[] for _ in range(m)]
        group_indegree = [0] * m

        for i in range(n):
            for j in beforeItems[i]:
                if group[i] == group[j]:
                    item_graph[j].append(i)
                    item_indegree[i] += 1
                else:
                    group_graph[group[j]].append(group[i])
                    group_indegree[group[i]] += 1

        def topo(graph, indegree):
            q = deque(i for i in range(len(graph)) if indegree[i] == 0)
            order = []

            while q:
                u = q.popleft()
                order.append(u)

                for v in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)

            return order if len(order) == len(graph) else []

        group_order = topo(group_graph, group_indegree)
        if not group_order:
            return []

        item_order = topo(item_graph, item_indegree)
        if not item_order:
            return []

        grouped_items = defaultdict(list)

        for item in item_order:
            grouped_items[group[item]].append(item)

        result = []
        for g in group_order:
            result.extend(grouped_items[g])

        return result if len(result) == n else []
```
