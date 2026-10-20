# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

# You can swap the characters at any pair of indices in the given pairs any number of times.

# Return the lexicographically smallest string that s can be changed to after using the swaps.



# Example 1:

# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# Example 2:

# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# Example 3:

# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination:
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"


# Constraints:

# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s only contains lower case English letters.
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
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        n = len(s)
        adj = [[] for _ in range(n)]

        for a, b in pairs:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * n
        res = list(s)

        for i in range(n):
            if visited[i]:
                continue

            stack = [i]
            visited[i] = True
            indices = []

            while stack:
                node = stack.pop()
                indices.append(node)

                for nei in adj[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)

            chars = sorted(s[idx] for idx in indices)
            indices.sort()

            for idx, ch in zip(indices, chars):
                res[idx] = ch

        return "".join(res)
```

### Optimal — Union Find (DSU)

python
```
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        n = len(s)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra = find(a)
            rb = find(b)

            if ra == rb:
                return

            if size[ra] < size[rb]:
                ra, rb = rb, ra

            parent[rb] = ra
            size[ra] += size[rb]

        for a, b in pairs:
            union(a, b)

        from collections import defaultdict
        groups = defaultdict(list)

        for i, ch in enumerate(s):
            groups[find(i)].append((ch, i))

        res = list(s)

        for group in groups.values():
            indices = sorted(i for _, i in group)
            chars = sorted(ch for ch, _ in group)

            for i, ch in zip(indices, chars):
                res[i] = ch

        return "".join(res)
```
