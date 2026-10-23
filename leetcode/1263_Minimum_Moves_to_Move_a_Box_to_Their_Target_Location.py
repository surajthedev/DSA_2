# A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

# The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.

# Your task is to move the box 'B' to the target position 'T' under the following rules:

# The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).
# The character '.' represents the floor which means a free cell to walk.
# The character '#' represents the wall which means an obstacle (impossible to walk there).
# There is only one box 'B' and one target cell 'T' in the grid.
# The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
# The player cannot walk through the box.
# Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.



# Example 1:


# Input: grid = [["#","#","#","#","#","#"],
#                ["#","T","#","#","#","#"],
#                ["#",".",".","B",".","#"],
#                ["#",".","#","#",".","#"],
#                ["#",".",".",".","S","#"],
#                ["#","#","#","#","#","#"]]
# Output: 3
# Explanation: We return only the number of times the box is pushed.
# Example 2:

# Input: grid = [["#","#","#","#","#","#"],
#                ["#","T","#","#","#","#"],
#                ["#",".",".","B",".","#"],
#                ["#","#","#","#",".","#"],
#                ["#",".",".",".","S","#"],
#                ["#","#","#","#","#","#"]]
# Output: -1
# Example 3:

# Input: grid = [["#","#","#","#","#","#"],
#                ["#","T",".",".","#","#"],
#                ["#",".","#","B",".","#"],
#                ["#",".",".",".",".","#"],
#                ["#",".",".",".","S","#"],
#                ["#","#","#","#","#","#"]]
# Output: 5
# Explanation: push the box down, left, left, up and up.


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 20
# grid contains only characters '.', '#', 'S', 'T', or 'B'.
# There is only one character 'S', 'B', and 'T' in the grid.
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
# ### Brute Force — BFS

python
```
from typing import List
from collections import deque

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    sx, sy = i, j
                elif grid[i][j] == 'B':
                    bx, by = i, j
                elif grid[i][j] == 'T':
                    tx, ty = i, j

        q = deque([(sx, sy, bx, by, 0)])
        visited = {(sx, sy, bx, by)}

        while q:
            px, py, bx, by, pushes = q.popleft()

            if (bx, by) == (tx, ty):
                return pushes

            for dx, dy in dirs:
                nx, ny = px + dx, py + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if grid[nx][ny] == '#':
                    continue

                nbx, nby = bx, by

                if (nx, ny) == (bx, by):
                    nbx, nby = bx + dx, by + dy

                    if not (0 <= nbx < m and 0 <= nby < n):
                        continue
                    if grid[nbx][nby] == '#':
                        continue

                    new_pushes = pushes + 1
                else:
                    new_pushes = pushes

                state = (nx, ny, nbx, nby)

                if state not in visited:
                    visited.add(state)
                    q.append((nx, ny, nbx, nby, new_pushes))

        return -1
```

### Optimal — BFS (Minimum Pushes)

python
```
from typing import List
from collections import deque

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    sx, sy = i, j
                elif grid[i][j] == 'B':
                    bx, by = i, j
                elif grid[i][j] == 'T':
                    tx, ty = i, j

        q = deque([(bx, by, sx, sy, 0)])
        visited = {(bx, by, sx, sy)}

        while q:
            bx, by, px, py, pushes = q.popleft()

            if (bx, by) == (tx, ty):
                return pushes

            for dx, dy in dirs:
                nbx, nby = bx + dx, by + dy
                npx, npy = bx - dx, by - dy

                if not (0 <= nbx < m and 0 <= nby < n):
                    continue
                if not (0 <= npx < m and 0 <= npy < n):
                    continue

                if grid[nbx][nby] == '#' or grid[npx][npy] == '#':
                    continue

                q2 = deque([(px, py)])
                seen = {(px, py)}
                can_reach = False

                while q2:
                    x, y = q2.popleft()

                    if (x, y) == (npx, npy):
                        can_reach = True
                        break

                    for ax, ay in dirs:
                        xx, yy = x + ax, y + ay

                        if not (0 <= xx < m and 0 <= yy < n):
                            continue
                        if grid[xx][yy] == '#' or (xx, yy) == (bx, by):
                            continue
                        if (xx, yy) not in seen:
                            seen.add((xx, yy))
                            q2.append((xx, yy))

                if can_reach:
                    state = (nbx, nby, bx, by)

                    if state not in visited:
                        visited.add(state)
                        q.append((nbx, nby, bx, by, pushes + 1))

        return -1
```
