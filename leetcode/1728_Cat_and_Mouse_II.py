# A game is played by a cat and a mouse named Cat and Mouse.

# The environment is represented by a grid of size rows x cols, where each element is a wall, floor, player (Cat, Mouse), or food.

# Players are represented by the characters 'C'(Cat),'M'(Mouse).
# Floors are represented by the character '.' and can be walked on.
# Walls are represented by the character '#' and cannot be walked on.
# Food is represented by the character 'F' and can be walked on.
# There is only one of each character 'C', 'M', and 'F' in grid.
# Mouse and Cat play according to the following rules:

# Mouse moves first, then they take turns to move.
# During each turn, Cat and Mouse can jump in one of the four directions (left, right, up, down). They cannot jump over the wall nor outside of the grid.
# catJump, mouseJump are the maximum lengths Cat and Mouse can jump at a time, respectively. Cat and Mouse can jump less than the maximum length.
# Staying in the same position is allowed.
# Mouse can jump over Cat.
# The game can end in 4 ways:

# If Cat occupies the same position as Mouse, Cat wins.
# If Cat reaches the food first, Cat wins.
# If Mouse reaches the food first, Mouse wins.
# If Mouse cannot get to the food within 1000 turns, Cat wins.
# Given a rows x cols matrix grid and two integers catJump and mouseJump, return true if Mouse can win the game if both Cat and Mouse play optimally, otherwise return false.



# Example 1:


# Input: grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
# Output: true
# Explanation: Cat cannot catch Mouse on its turn nor can it get the food before Mouse.
# Example 2:


# Input: grid = ["M.C...F"], catJump = 1, mouseJump = 4
# Output: true
# Example 3:

# Input: grid = ["M.C...F"], catJump = 1, mouseJump = 3
# Output: false


# Constraints:

# rows == grid.length
# cols = grid[i].length
# 1 <= rows, cols <= 8
# grid[i][j] consist only of characters 'C', 'M', 'F', '.', and '#'.
# There is only one of each character 'C', 'M', and 'F' in grid.
# 1 <= catJump, mouseJump <= 8
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
# ### Brute Force (DFS + Memoization)

python

```python

from functools import lru_cache

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m, n = len(grid), len(grid[0])
        cells = [(r, c) for r in range(m) for c in range(n)
                 if grid[r][c] != '#']

        pos = {p: i for i, p in enumerate(cells)}
        M = C = F = -1

        for i, (r, c) in enumerate(cells):
            if grid[r][c] == 'M':
                M = i
            elif grid[r][c] == 'C':
                C = i
            elif grid[r][c] == 'F':
                F = i

        def moves(p, jump):
            r, c = cells[p]
            res = [p]

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                for d in range(1, jump + 1):
                    nr, nc = r + dr * d, c + dc * d

                    if not (0 <= nr < m and 0 <= nc < n):
                        break
                    if grid[nr][nc] == '#':
                        break

                    res.append(pos[(nr, nc)])

            return res

        mouse_moves = [moves(i, mouseJump) for i in range(len(cells))]
        cat_moves = [moves(i, catJump) for i in range(len(cells))]

        @lru_cache(None)
        def dfs(mouse, cat, turn, steps):
            if mouse == cat or cat == F:
                return False
            if mouse == F:
                return True
            if steps >= 2000:
                return False

            if turn == 0:
                for nxt in mouse_moves[mouse]:
                    if dfs(nxt, cat, 1, steps + 1):
                        return True
                return False
            else:
                for nxt in cat_moves[cat]:
                    if not dfs(mouse, nxt, 0, steps + 1):
                        return False
                return True

        return dfs(M, C, 0, 0)
```

### Optimal Solution (Minimax + BFS + Memoization)

Recommended for LeetCodepython

```python

from collections import deque
from functools import lru_cache

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        rows, cols = len(grid), len(grid[0])

        cells = []
        mouse = cat = food = -1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '#':
                    idx = len(cells)
                    cells.append((r, c))

                    if grid[r][c] == 'M':
                        mouse = idx
                    elif grid[r][c] == 'C':
                        cat = idx
                    elif grid[r][c] == 'F':
                        food = idx

        n = len(cells)

        def get_moves(jump):
            result = [[] for _ in range(n)]
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for i, (r, c) in enumerate(cells):
                result[i].append(i)

                for dr, dc in directions:
                    for d in range(1, jump + 1):
                        nr = r + dr * d
                        nc = c + dc * d

                        if not (0 <= nr < rows and 0 <= nc < cols):
                            break
                        if grid[nr][nc] == '#':
                            break

                        for j, p in enumerate(cells):
                            if p == (nr, nc):
                                result[i].append(j)
                                break

            return result

        mouse_moves = get_moves(mouseJump)
        cat_moves = get_moves(catJump)

        @lru_cache(None)
        def dfs(m, c, turn, t):
            if m == c or c == food or t >= 1000:
                return False

            if m == food:
                return True

            if turn == 0:
                for nxt in mouse_moves[m]:
                    if dfs(nxt, c, 1, t + 1):
                        return True
                return False

            else:
                for nxt in cat_moves[c]:
                    if not dfs(m, nxt, 0, t + 1):
                        return False
                return True

        return dfs(mouse, cat, 0, 0)
```
