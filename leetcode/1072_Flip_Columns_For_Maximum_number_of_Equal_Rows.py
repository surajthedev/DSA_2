# You are given an m x n binary matrix matrix.

# You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

# Return the maximum number of rows that have all values equal after some number of flips.



# Example 1:

# Input: matrix = [[0,1],[1,1]]
# Output: 1
# Explanation: After flipping no values, 1 row has all values equal.
# Example 2:

# Input: matrix = [[0,1],[1,0]]
# Output: 2
# Explanation: After flipping values in the first column, both rows have equal values.
# Example 3:

# Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
# Output: 2
# Explanation: After flipping values in the first two columns, the last two rows have equal values.


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is either 0 or 1.
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
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0

        for row in matrix:
            count = 0

            for other in matrix:
                if all(
                    other[j] == row[j] or other[j] != row[j]
                    for j in range(n)
                ):
                    pattern = tuple(x ^ row[0] for x in other)
                    target = tuple(x ^ row[0] for x in row)

                    if pattern == target:
                        count += 1

            ans = max(ans, count)

        return ans
```

### Optimal (Hash Map)

python
```
from collections import Counter

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        count = Counter()

        for row in matrix:
            if row[0] == 0:
                pattern = tuple(row)
            else:
                pattern = tuple(1 - x for x in row)

            count[pattern] += 1

        return max(count.values())
```
