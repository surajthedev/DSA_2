# Given a matrix and a target, return the number of non-empty submatrices that sum to target.

# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.



# Example 1:


# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.
# Example 2:

# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
# Example 3:

# Input: matrix = [[904]], target = 0
# Output: 0


# Constraints:

# 1 <= matrix.length <= 100
# 1 <= matrix[0].length <= 100
# -1000 <= matrix[i][j] <= 1000
# -10^8 <= target <= 10^8
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
# ### Brute Force

python
```
class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0

        for r1 in range(m):
            for c1 in range(n):
                for r2 in range(r1, m):
                    for c2 in range(c1, n):
                        total = 0

                        for i in range(r1, r2 + 1):
                            for j in range(c1, c2 + 1):
                                total += matrix[i][j]

                        if total == target:
                            ans += 1

        return ans
```

### Optimal (Prefix Sum + Hash Map)

python
```
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0

        for top in range(m):
            col_sum = [0] * n

            for bottom in range(top, m):
                for c in range(n):
                    col_sum[c] += matrix[bottom][c]

                prefix = 0
                count = defaultdict(int)
                count[0] = 1

                for x in col_sum:
                    prefix += x
                    ans += count[prefix - target]
                    count[prefix] += 1

        return ans
```
