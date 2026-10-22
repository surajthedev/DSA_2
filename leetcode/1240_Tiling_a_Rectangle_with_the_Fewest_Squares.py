# Given a rectangle of size n x m, return the minimum number of integer-sided squares that tile the rectangle.



# Example 1:



# Input: n = 2, m = 3
# Output: 3
# Explanation: 3 squares are necessary to cover the rectangle.
# 2 (squares of 1x1)
# 1 (square of 2x2)
# Example 2:



# Input: n = 5, m = 8
# Output: 5
# Example 3:



# Input: n = 11, m = 13
# Output: 6


# Constraints:

# 1 <= n, m <= 13
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
# ### Brute Force (Backtracking)

python
```
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n > m:
            n, m = m, n

        heights = [0] * m
        ans = n * m

        def dfs(count):
            nonlocal ans

            if count >= ans:
                return

            if all(h == n for h in heights):
                ans = count
                return

            min_height = min(heights)
            idx = heights.index(min_height)

            width = 0
            while (
                idx + width < m
                and heights[idx + width] == min_height
            ):
                width += 1

            max_size = min(width, n - min_height)

            for size in range(max_size, 0, -1):
                for j in range(idx, idx + size):
                    heights[j] += size

                dfs(count + 1)

                for j in range(idx, idx + size):
                    heights[j] -= size

        dfs(0)
        return ans
```

### Optimal (Backtracking + Pruning)

python
```
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n > m:
            n, m = m, n

        if n == m:
            return 1

        heights = [0] * m
        ans = n * m

        def dfs(count):
            nonlocal ans

            if count >= ans:
                return

            idx = 0
            min_height = n

            for i, h in enumerate(heights):
                if h < min_height:
                    min_height = h
                    idx = i

            if min_height == n:
                ans = count
                return

            end = idx
            while end < m and heights[end] == min_height:
                end += 1

            max_size = min(end - idx, n - min_height)

            for size in range(max_size, 0, -1):
                for j in range(idx, idx + size):
                    heights[j] += size

                dfs(count + 1)

                for j in range(idx, idx + size):
                    heights[j] -= size

        dfs(0)
        return ans
```
