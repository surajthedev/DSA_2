# A certain bug's home is on the x-axis at position x. Help them get there from position 0.

# The bug jumps according to the following rules:

# It can jump exactly a positions forward (to the right).
# It can jump exactly b positions backward (to the left).
# It cannot jump backward twice in a row.
# It cannot jump to any forbidden positions.
# The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

# Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.



# Example 1:

# Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
# Output: 3
# Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
# Example 2:

# Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
# Output: -1
# Example 3:

# Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
# Output: 2
# Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.


# Constraints:

# 1 <= forbidden.length <= 1000
# 1 <= a, b, forbidden[i] <= 2000
# 0 <= x <= 2000
# All the elements in forbidden are distinct.
# Position x is not forbidden.
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
# ### Brute Force — BFS

python

```python
from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        q = deque([(0, 0, False)])
        visited = {(0, False)}

        while q:
            pos, jumps, last_back = q.popleft()

            if pos == x:
                return jumps

            forward = pos + a

            if forward <= 6000 and forward not in forbidden and (forward, False) not in visited:
                visited.add((forward, False))
                q.append((forward, jumps + 1, False))

            backward = pos - b

            if not last_back and backward >= 0 and backward not in forbidden and (backward, True) not in visited:
                visited.add((backward, True))
                q.append((backward, jumps + 1, True))

        return -1
```

### Optimal Approach — BFS (O(6000))

python

```python
from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)

        limit = max(max(forbidden) + a + b, x + b + a, 6000)

        q = deque([(0, 0, 0)])
        visited = {(0, 0)}

        while q:
            pos, jumps, last_back = q.popleft()

            if pos == x:
                return jumps

            forward = pos + a

            if forward <= limit and forward not in forbidden and (forward, 0) not in visited:
                visited.add((forward, 0))
                q.append((forward, jumps + 1, 0))

            backward = pos - b

            if last_back == 0 and backward >= 0 and backward not in forbidden and (backward, 1) not in visited:
                visited.add((backward, 1))
                q.append((backward, jumps + 1, 1))

        return -1
```
