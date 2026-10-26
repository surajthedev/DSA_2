# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.



# Example 1:


# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than or equal to 4 is 2 as shown.
# Example 2:

# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
# Output: 0


# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 300
# 0 <= mat[i][j] <= 104
# 0 <= threshold <= 105
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
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0

        for size in range(1, min(m, n) + 1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    total = sum(
                        mat[r][c]
                        for r in range(i, i + size)
                        for c in range(j, j + size)
                    )

                    if total <= threshold:
                        ans = size

        return ans
```

### Optimal (Prefix Sum + Binary Search)

python

```

class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        def exists(size):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    total = (
                        prefix[i + size][j + size]
                        - prefix[i][j + size]
                        - prefix[i + size][j]
                        + prefix[i][j]
                    )

                    if total <= threshold:
                        return True

            return False

        left, right = 0, min(m, n)

        while left < right:
            mid = (left + right + 1) // 2

            if exists(mid):
                left = mid
            else:
                right = mid - 1

        return left
```
