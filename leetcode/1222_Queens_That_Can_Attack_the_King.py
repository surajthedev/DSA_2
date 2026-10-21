# On a 0-indexed 8 x 8 chessboard, there can be multiple black queens and one white king.

# You are given a 2D integer array queens where queens[i] = [xQueeni, yQueeni] represents the position of the ith black queen on the chessboard. You are also given an integer array king of length 2 where king = [xKing, yKing] represents the position of the white king.

# Return the coordinates of the black queens that can directly attack the king. You may return the answer in any order.



# Example 1:


# Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
# Output: [[0,1],[1,0],[3,3]]
# Explanation: The diagram above shows the three queens that can directly attack the king and the three queens that cannot attack the king (i.e., marked with red dashes).
# Example 2:


# Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
# Output: [[2,2],[3,4],[4,4]]
# Explanation: The diagram above shows the three queens that can directly attack the king and the three queens that cannot attack the king (i.e., marked with red dashes).


# Constraints:

# 1 <= queens.length < 64
# queens[i].length == king.length == 2
# 0 <= xQueeni, yQueeni, xKing, yKing < 8
# All the given positions are unique.
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
from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []

        for qx, qy in queens:
            kx, ky = king

            if qx == kx or qy == ky or abs(qx - kx) == abs(qy - ky):
                dx = 0 if qx == kx else (1 if qx > kx else -1)
                dy = 0 if qy == ky else (1 if qy > ky else -1)

                x, y = kx + dx, ky + dy

                while x != qx or y != qy:
                    if [x, y] in queens:
                        break
                    x += dx
                    y += dy
                else:
                    ans.append([qx, qy])

        return ans
```

### Optimal Solution

python
```
from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queen_set = {tuple(q) for q in queens}
        ans = []

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for dx, dy in directions:
            x, y = king

            while 0 <= x + dx < 8 and 0 <= y + dy < 8:
                x += dx
                y += dy

                if (x, y) in queen_set:
                    ans.append([x, y])
                    break

        return ans
```
