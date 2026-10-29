# You are given an undirected tree with n nodes labeled 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.

# You are also given a string s of length n consisting of lowercase English letters, where s[i] represents the character assigned to node i.

# You are also given a string array queries, where each queries[i] is either:

# "update ui c": Change the character at node ui to c. Formally, update s[ui] = c.
# "query ui vi": Determine whether the string formed by the characters on the unique path from ui to vi (inclusive) can be rearranged into a palindrome.
# Return a boolean array answer, where answer[j] is true if the jth query of type "query ui vi"​​​​​​​ can be rearranged into a palindrome, and false otherwise.



# Example 1:

# Input: n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]

# Output: [true,false]

# Explanation:

# "query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form "aca", a palindrome. Thus, answer[0] = true.
# "update 1 b": Update node 1 to 'b', now s = "abc".
# "query 0 2": Path characters are "abc", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
# Thus, answer = [true, false].

# Example 2:

# Input: n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]

# Output: [false,false,true]

# Explanation:

# "query 1 2": Path 1 → 0 → 2 gives "bac", which cannot be rearranged to form a palindrome. Thus, answer[0] = false.
# "update 0 b": Update node 0 to 'b', now s = "bbca".
# "query 2 3": Path 2 → 0 → 3 gives "cba", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
# "update 3 a": Update node 3 to 'a', s = "bbca".
# "query 1 3": Path 1 → 0 → 3 gives "bba", which can be rearranged to form "bab", a palindrome. Thus, answer[2] = true.
# Thus, answer = [false, false, true].



# Constraints:

# 1 <= n == s.length <= 5 * 104
# edges.length == n - 1
# edges[i] = [ui, vi]
# 0 <= ui, vi <= n - 1
# s consists of lowercase English letters.
# The input is generated such that edges represents a valid tree.
# 1 <= queries.length <= 5 * 104​​​​​​​
# queries[i] = "update ui c" or
# queries[i] = "query ui vi"
# 0 <= ui, vi <= n - 1
# c is a lowercase English letter.
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
# ## Brute Force

python

```

class Solution:
    def palindromePath(self, n, edges, s, queries):
        from collections import defaultdict, deque

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        chars = list(s)
        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                chars[u] = parts[2]

            else:
                u, v = int(parts[1]), int(parts[2])

                parent = {u: -1}
                queue = deque([u])

                while queue:
                    node = queue.popleft()
                    if node == v:
                        break

                    for nei in graph[node]:
                        if nei not in parent:
                            parent[nei] = node
                            queue.append(nei)

                mask = 0
                node = v

                while node != -1:
                    mask ^= 1 << (ord(chars[node]) - ord('a'))
                    if node == u:
                        break
                    node = parent[node]

                ans.append(mask == 0 or (mask & (mask - 1)) == 0)

        return ans
```

## Optimal — HLD + Segment Tree

python

```

class Solution:
    def palindromePath(self, n, edges, s, queries):
        from collections import defaultdict

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        chars = list(s)
        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        order = [0]
        for u in order:
            for v in graph[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        for u in reversed(order):
            largest = 0
            for v in graph[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in graph[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        seg = [0] * (2 * n)

        for u in range(n):
            seg[n + pos[u]] = 1 << (ord(chars[u]) - ord('a'))

        for i in range(n - 1, 0, -1):
            seg[i] = seg[i * 2] ^ seg[i * 2 + 1]

        def update(p, value):
            p += n
            seg[p] = value
            p //= 2

            while p:
                seg[p] = seg[p * 2] ^ seg[p * 2 + 1]
                p //= 2

        def range_query(l, r):
            result = 0
            l += n
            r += n + 1

            while l < r:
                if l & 1:
                    result ^= seg[l]
                    l += 1
                if r & 1:
                    r -= 1
                    result ^= seg[r]

                l //= 2
                r //= 2

            return result

        def path_query(u, v):
            mask = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                mask ^= range_query(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            mask ^= range_query(pos[u], pos[v])
            return mask

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                chars[u] = parts[2]
                update(pos[u], 1 << (ord(chars[u]) - ord('a')))
            else:
                u, v = int(parts[1]), int(parts[2])
                mask = path_query(u, v)
                ans.append(mask == 0 or (mask & (mask - 1)) == 0)

        return ans
```
