# You have a cubic storeroom where the width, length, and height of the room are all equal to n units. You are asked to place n boxes in this room where each box is a cube of unit side length. There are however some rules to placing the boxes:

# You can place the boxes anywhere on the floor.
# If box x is placed on top of the box y, then each side of the four vertical sides of the box y must either be adjacent to another box or to a wall.
# Given an integer n, return the minimum possible number of boxes touching the floor.



# Example 1:



# Input: n = 3
# Output: 3
# Explanation: The figure above is for the placement of the three boxes.
# These boxes are placed in the corner of the room, where the corner is on the left side.
# Example 2:



# Input: n = 4
# Output: 3
# Explanation: The figure above is for the placement of the four boxes.
# These boxes are placed in the corner of the room, where the corner is on the left side.
# Example 3:



# Input: n = 10
# Output: 6
# Explanation: The figure above is for the placement of the ten boxes.
# These boxes are placed in the corner of the room, where the corner is on the back side.


# Constraints:

# 1 <= n <= 109
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

class Solution:
    def minimumBoxes(self, n: int) -> int:
        floor = 0
        height = 0
        used = 0

        while used + (height + 1) * (height + 2) // 2 <= n:
            height += 1
            floor += height
            used += height * (height + 1) * (height + 2) // 6

        remaining = n - used

        extra = 0
        while remaining > 0:
            extra += 1
            remaining -= extra

        return floor + extra
```

- Time Complexity: O(∛N + √N)
- Space Complexity: O(1)

### 2. Optimal — Python

Recommendedpython

```python

class Solution:
    def minimumBoxes(self, n: int) -> int:
        height = 0
        used = 0
        floor = 0

        while True:
            next_height = height + 1
            total = next_height * (next_height + 1) * (next_height + 2) // 6

            if total > n:
                break

            height = next_height
            used = total
            floor = height * (height + 1) // 2

        remaining = n - used

        left, right = 0, height + 1

        while left < right:
            mid = (left + right) // 2

            if mid * (mid + 1) // 2 >= remaining:
                right = mid
            else:
                left = mid + 1

        return floor + left
```

- Time Complexity: O(∛N + log N)
- Space Complexity: O(1)
