# Alice is throwing n darts on a very large wall. You are given an array darts where darts[i] = [xi, yi] is the position of the ith dart that Alice threw on the wall.

# Bob knows the positions of the n darts on the wall. He wants to place a dartboard of radius r on the wall so that the maximum number of darts that Alice throws lie on the dartboard.

# Given the integer r, return the maximum number of darts that can lie on the dartboard.



# Example 1:


# Input: darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
# Output: 4
# Explanation: Circle dartboard with center in (0,0) and radius = 2 contain all points.
# Example 2:


# Input: darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
# Output: 5
# Explanation: Circle dartboard with center in (0,4) and radius = 5 contain all points except the point (7,8).


# Constraints:

# 1 <= darts.length <= 100
# darts[i].length == 2
# -104 <= xi, yi <= 104
# All the darts are unique
# 1 <= r <= 5000
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
# ### 1. Brute Force — Python

python

```python
import math

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        n = len(darts)
        ans = 1

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = darts[i]
                x2, y2 = darts[j]

                d = math.hypot(x2 - x1, y2 - y1)

                if d > 2 * r:
                    continue

                mx = (x1 + x2) / 2
                my = (y1 + y2) / 2

                h = math.sqrt(r * r - (d / 2) ** 2)

                dx = (y2 - y1) * h / d
                dy = (x1 - x2) * h / d

                for cx, cy in [(mx + dx, my + dy),
                               (mx - dx, my - dy)]:

                    count = 0

                    for x, y in darts:
                        if (x - cx) ** 2 + (y - cy) ** 2 <= r * r + 1e-7:
                            count += 1

                    ans = max(ans, count)

        return ans
```

Time Complexity: $O(N^3)$

Space Complexity: $O(1)$

### 2. Optimal — Python (Geometry + Circle Centers)

python

```python
import math

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        n = len(darts)
        ans = 1
        r2 = r * r

        for i in range(n):
            x1, y1 = darts[i]

            for j in range(i + 1, n):
                x2, y2 = darts[j]

                dx = x2 - x1
                dy = y2 - y1

                d2 = dx * dx + dy * dy

                if d2 > 4 * r2:
                    continue

                d = math.sqrt(d2)

                mx = (x1 + x2) / 2
                my = (y1 + y2) / 2

                h = math.sqrt(max(0, r2 - d2 / 4))

                ox = -dy * h / d
                oy = dx * h / d

                centers = [
                    (mx + ox, my + oy),
                    (mx - ox, my - oy)
                ]

                for cx, cy in centers:
                    count = 0

                    for x, y in darts:
                        if (x - cx) ** 2 + (y - cy) ** 2 <= r2 + 1e-7:
                            count += 1

                    ans = max(ans, count)

        return ans
```

Time Complexity: $O(N^3)$

Space Complexity: $O(1)$
