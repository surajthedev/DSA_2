# You are given two integer arrays, source and target, both of length n. You are also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates that you are allowed to swap the elements at index ai and index bi (0-indexed) of array source. Note that you can swap elements at a specific pair of indices multiple times and in any order.

# The Hamming distance of two arrays of the same length, source and target, is the number of positions where the elements are different. Formally, it is the number of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).

# Return the minimum Hamming distance of source and target after performing any amount of swap operations on array source.



# Example 1:

# Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
# Output: 1
# Explanation: source can be transformed the following way:
# - Swap indices 0 and 1: source = [2,1,3,4]
# - Swap indices 2 and 3: source = [2,1,4,3]
# The Hamming distance of source and target is 1 as they differ in 1 position: index 3.
# Example 2:

# Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
# Output: 2
# Explanation: There are no allowed swaps.
# The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.
# Example 3:

# Input: source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
# Output: 0


# Constraints:

# n == source.length == target.length
# 1 <= n <= 105
# 1 <= source[i], target[i] <= 105
# 0 <= allowedSwaps.length <= 105
# allowedSwaps[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
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
# ### 1. Brute Force Approach (Repeated Swapping)

python

```python
from typing import List

class Solution:
    def minimumHammingDistance(
        self,
        source: List[int],
        target: List[int],
        allowedSwaps: List[List[int]]
    ) -> int:

        n = len(source)
        changed = True

        while changed:
            changed = False

            for a, b in allowedSwaps:
                if source[a] != source[b]:
                    source[a], source[b] = source[b], source[a]
                    changed = True

        return sum(source[i] != target[i] for i in range(n))
```

### 2. Optimal Approach (Union Find + HashMap)

python

```python
from typing import List
from collections import Counter

class Solution:
    def minimumHammingDistance(
        self,
        source: List[int],
        target: List[int],
        allowedSwaps: List[List[int]]
    ) -> int:

        n = len(source)
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return

            if rank[px] < rank[py]:
                px, py = py, px

            parent[py] = px

            if rank[px] == rank[py]:
                rank[px] += 1

        for a, b in allowedSwaps:
            union(a, b)

        groups = {}

        for i in range(n):
            root = find(i)

            if root not in groups:
                groups[root] = Counter()

            groups[root][source[i]] += 1

        ans = 0

        for i in range(n):
            root = find(i)

            if groups[root][target[i]] > 0:
                groups[root][target[i]] -= 1
            else:
                ans += 1

        return ans
```

Time Complexity: $O((n+m)\alpha(n))$

Space Complexity: $O(n)$
