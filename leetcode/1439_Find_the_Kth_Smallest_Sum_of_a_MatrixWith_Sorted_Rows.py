# You are given an m x n matrix mat that has its rows sorted in non-decreasing order and an integer k.

# You are allowed to choose exactly one element from each row to form an array.

# Return the kth smallest array sum among all possible arrays.



# Example 1:

# Input: mat = [[1,3,11],[2,4,6]], k = 5
# Output: 7
# Explanation: Choosing one element from each row, the first k smallest sum are:
# [1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.
# Example 2:

# Input: mat = [[1,3,11],[2,4,6]], k = 9
# Output: 17
# Example 3:

# Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
# Output: 9
# Explanation: Choosing one element from each row, the first k smallest sum are:
# [1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.


# Constraints:

# m == mat.length
# n == mat.length[i]
# 1 <= m, n <= 40
# 1 <= mat[i][j] <= 5000
# 1 <= k <= min(200, nm)
# mat[i] is a non-decreasing array.
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
# ### 1. Brute Force Approach — Generate All Combinations

python

```python
from itertools import product

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        sums = []

        for combination in product(*mat):
            sums.append(sum(combination))

        sums.sort()

        return sums[k - 1]
```

Time Complexity: O(n^m × m + n^m log(n^m))

Space Complexity: O(n^m)

### 2. Optimal Approach — Min Heap (K-way Merge)

python

```python
import heapq

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        sums = mat[0][:]

        for row in mat[1:]:
            heap = []

            for i, a in enumerate(sums):
                for j, b in enumerate(row):
                    heapq.heappush(heap, (a + b, i, j))

            sums = []

            for _ in range(min(k, len(heap))):
                sums.append(heapq.heappop(heap)[0])

        return sums[k - 1]
```

Time Complexity: O(m × n × k × log(n × k))

Space Complexity: O(n × k)
