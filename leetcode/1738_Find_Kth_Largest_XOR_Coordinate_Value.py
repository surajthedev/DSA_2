# You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.

# The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).

# Find the kth largest value (1-indexed) of all the coordinates of matrix.



# Example 1:

# Input: matrix = [[5,2],[1,6]], k = 1
# Output: 7
# Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.
# Example 2:

# Input: matrix = [[5,2],[1,6]], k = 2
# Output: 5
# Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.
# Example 3:

# Input: matrix = [[5,2],[1,6]], k = 3
# Output: 4
# Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 0 <= matrix[i][j] <= 106
# 1 <= k <= m * n
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
# ### 1. Brute Force — Python

python

```python

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        values = []

        for i in range(m):
            for j in range(n):
                xor = 0

                for r in range(i + 1):
                    for c in range(j + 1):
                        xor ^= matrix[r][c]

                values.append(xor)

        values.sort(reverse=True)
        return values[k - 1]
```

- Time Complexity: O(M² × N² + MN log(MN))
- Space Complexity: O(MN)

### 2. Optimal — Python

Recommendedpython

```python

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        values = []

        for i in range(m):
            for j in range(n):
                if i > 0:
                    matrix[i][j] ^= matrix[i - 1][j]

                if j > 0:
                    matrix[i][j] ^= matrix[i][j - 1]

                if i > 0 and j > 0:
                    matrix[i][j] ^= matrix[i - 1][j - 1]

                values.append(matrix[i][j])

        values.sort(reverse=True)

        return values[k - 1]
```

- Time Complexity: O(MN + MN log(MN))
- Space Complexity: O(MN)
