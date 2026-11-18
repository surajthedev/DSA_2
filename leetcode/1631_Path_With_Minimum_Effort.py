# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.



# Example 1:



# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
# Example 2:



# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
# Example 3:


# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.


# Constraints:

# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 106
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
# ### 1. Brute Force Approach (Binary Search + BFS)

python

```python
from typing import List
from collections import deque

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        def canReach(limit):
            q = deque([(0, 0)])
            visited = {(0, 0)}

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while q:
                r, c = q.popleft()

                if r == rows - 1 and c == cols - 1:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        diff = abs(heights[r][c] - heights[nr][nc])

                        if diff <= limit and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            q.append((nr, nc))

            return False

        left, right = 0, 10**6

        while left < right:
            mid = (left + right) // 2

            if canReach(mid):
                right = mid
            else:
                left = mid + 1

        return left
```

### 2. Optimal Approach (Dijkstra's Algorithm)

python

```python
import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while heap:
            effort, r, c = heapq.heappop(heap)

            if r == rows - 1 and c == cols - 1:
                return effort

            if effort > dist[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(
                        effort,
                        abs(heights[r][c] - heights[nr][nc])
                    )

                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))

        return 0
```

### Complexity

| Approach | Time Complexity | Space Complexity |
| --- | --- | --- |
| Binary Search + BFS | O(R × C × log H) | O(R × C) |
| Dijkstra | O(R × C × log(R × C)) | O(R × C) |

`R = rows`, `C = columns`, `H = maximum possible height difference`.
