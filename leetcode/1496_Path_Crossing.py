# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.



# Example 1:


# Input: path = "NES"
# Output: false
# Explanation: Notice that the path doesn't cross any point more than once.
# Example 2:


# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.


# Constraints:

# 1 <= path.length <= 104
# path[i] is either 'N', 'S', 'E', or 'W'.
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
# ### 1. Brute Force — O(n²)

python

```python

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = [(0, 0)]

        for move in path:
            if move == 'N':
                y += 1
            elif move == 'S':
                y -= 1
            elif move == 'E':
                x += 1
            else:
                x -= 1

            if (x, y) in visited:
                return True

            visited.append((x, y))

        return False
```

### 2. Optimal — O(n)

python

```python

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(0, 0)}

        directions = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }

        for move in path:
            dx, dy = directions[move]
            x += dx
            y += dy

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False
```s
