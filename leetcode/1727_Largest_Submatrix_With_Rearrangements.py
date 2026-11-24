# You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

# Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.



# Example 1:


# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.
# Example 2:


# Input: matrix = [[1,0,1,0,1]]
# Output: 3
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 3.
# Example 3:

# Input: matrix = [[1,1,0],[1,0,1]]
# Output: 2
# Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m * n <= 105
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
#
#
#
#
#
#
#
#
#
# ### 1. Brute Force Approach

python

```python
from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            for j in range(n):
                temp = heights[:]
                temp.sort(reverse=True)

                for k in range(n):
                    ans = max(ans, temp[k] * (k + 1))

        return ans
```

### 2. Optimal Approach (Greedy + Sorting)

python

```python
from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            sorted_heights = sorted(heights, reverse=True)

            for j in range(n):
                ans = max(ans, sorted_heights[j] * (j + 1))

        return ans
```

Time Complexity:

- Brute Force: $O(mn^2 \log n)$
- Optimal: $O(mn \log n)$

Space Complexity: $O(n)$ excluding sorting space.
