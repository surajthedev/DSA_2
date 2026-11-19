# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

# Note that points on the edge of a vertical area are not considered included in the area.



# Example 1:

# ​
# Input: points = [[8,7],[9,9],[7,4],[9,7]]
# Output: 1
# Explanation: Both the red and the blue area are optimal.
# Example 2:

# Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# Output: 3


# Constraints:

# n == points.length
# 2 <= n <= 105
# points[i].length == 2
# 0 <= xi, yi <= 109
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
# ### 1. Brute Force Solution

python

```python
from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = [p[0] for p in points]
        ans = 0

        for i in range(len(x)):
            for j in range(i + 1, len(x)):
                if x[i] != x[j]:
                    ans = max(ans, abs(x[i] - x[j]))

        return ans
```

Time Complexity: O(n²)

### 2. Optimal Solution

python

```python
from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = sorted(p[0] for p in points)

        ans = 0

        for i in range(1, len(x)):
            ans = max(ans, x[i] - x[i - 1])

        return ans
```

Time Complexity: O(n log n)

Space Complexity: O(n)
