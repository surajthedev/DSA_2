# You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

# If isWater[i][j] == 0, cell (i, j) is a land cell.
# If isWater[i][j] == 1, cell (i, j) is a water cell.
# You must assign each cell a height in a way that follows these rules:

# The height of each cell must be non-negative.
# If the cell is a water cell, its height must be 0.
# Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
# Find an assignment of heights such that the maximum height in the matrix is maximized.

# Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.



# Example 1:



# Input: isWater = [[0,1],[0,0]]
# Output: [[1,0],[2,1]]
# Explanation: The image shows the assigned heights of each cell.
# The blue cell is the water cell, and the green cells are the land cells.
# Example 2:



# Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
# Output: [[1,1,0],[0,1,1],[1,2,2]]
# Explanation: A height of 2 is the maximum possible height of any assignment.
# Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.


# Constraints:

# m == isWater.length
# n == isWater[i].length
# 1 <= m, n <= 1000
# isWater[i][j] is 0 or 1.
# There is at least one water cell.
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
#
#
#
#
# ### 1. Brute Force Approach (Repeated Relaxation)

Time Complexity: $O((m \times n)^2)$ worst case.

python

```python
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])

        height = [[float('inf')] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0

        changed = True

        while changed:
            changed = False

            for i in range(m):
                for j in range(n):
                    if isWater[i][j] == 1:
                        continue

                    best = float('inf')

                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        x, y = i + dx, j + dy

                        if 0 <= x < m and 0 <= y < n:
                            best = min(best, height[x][y] + 1)

                    if best < height[i][j]:
                        height[i][j] = best
                        changed = True

        return height
```

### 2. Optimal Approach (Multi-Source BFS)

O(m × n) Time | O(m × n) Spacepython

```python
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])

        height = [[-1] * n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    q.append((i, j))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1
                    q.append((nx, ny))

        return height
```
