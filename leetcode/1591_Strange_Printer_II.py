# There is a strange printer with the following two special requirements:

# On each turn, the printer will print a solid rectangular pattern of a single color on the grid. This will cover up the existing colors in the rectangle.
# Once the printer has used a color for the above operation, the same color cannot be used again.
# You are given a m x n matrix targetGrid, where targetGrid[row][col] is the color in the position (row, col) of the grid.

# Return true if it is possible to print the matrix targetGrid, otherwise, return false.



# Example 1:


# Input: targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
# Output: true
# Example 2:


# Input: targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
# Output: true
# Example 3:

# Input: targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
# Output: false
# Explanation: It is impossible to form targetGrid because it is not allowed to print the same color in different turns.


# Constraints:

# m == targetGrid.length
# n == targetGrid[i].length
# 1 <= m, n <= 60
# 1 <= targetGrid[row][col] <= 60
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
# **Brute Force — Recursive (Backtracking)**

```
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        colors = set(sum(targetGrid, []))

        def check(color):
            cells = [(i, j) for i in range(m) for j in range(n)
                     if targetGrid[i][j] == color]

            if not cells:
                return False

            r1 = min(i for i, j in cells)
            r2 = max(i for i, j in cells)
            c1 = min(j for i, j in cells)
            c2 = max(j for i, j in cells)

            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if targetGrid[i][j] != color:
                        return False

            return True

        def backtrack(remaining):
            if not remaining:
                return True

            for color in list(remaining):
                if check(color):
                    cells = [(i, j) for i in range(m) for j in range(n)
                             if targetGrid[i][j] == color]

                    for i, j in cells:
                        targetGrid[i][j] = 0

                    if backtrack(remaining - {color}):
                        return True

                    for i, j in cells:
                        targetGrid[i][j] = color

            return False

        return backtrack(colors)```

**Optimal — O(C × (m × n + C))**

```
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])

        bounds = {}

        for i in range(m):
            for j in range(n):
                color = targetGrid[i][j]

                if color not in bounds:
                    bounds[color] = [i, i, j, j]
                else:
                    bounds[color][0] = min(bounds[color][0], i)
                    bounds[color][1] = max(bounds[color][1], i)
                    bounds[color][2] = min(bounds[color][2], j)
                    bounds[color][3] = max(bounds[color][3], j)

        graph = {color: set() for color in bounds}
        indegree = {color: 0 for color in bounds}

        for color, (r1, r2, c1, c2) in bounds.items():
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    other = targetGrid[i][j]

                    if other != color and other not in graph[color]:
                        graph[color].add(other)
                        indegree[other] += 1

        queue = [color for color in indegree if indegree[color] == 0]
        count = 0

        while queue:
            color = queue.pop()
            count += 1

            for other in graph[color]:
                indegree[other] -= 1

                if indegree[other] == 0:
                    queue.append(other)

        return count == len(bounds)```
