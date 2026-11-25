# You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.

# Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.

# Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.



# Example 1:

# Input: lowLimit = 1, highLimit = 10
# Output: 2
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
# Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
# Box 1 has the most number of balls with 2 balls.
# Example 2:

# Input: lowLimit = 5, highLimit = 15
# Output: 2
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
# Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
# Boxes 5 and 6 have the most number of balls with 2 balls in each.
# Example 3:

# Input: lowLimit = 19, highLimit = 28
# Output: 2
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
# Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
# Box 10 has the most number of balls with 2 balls.


# Constraints:

# 1 <= lowLimit <= highLimit <= 105
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

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}

        for num in range(lowLimit, highLimit + 1):
            digit_sum = sum(int(d) for d in str(num))

            boxes[digit_sum] = boxes.get(digit_sum, 0) + 1

        return max(boxes.values())
```

- Time Complexity: O(N × D)
- Space Complexity: O(D × N) (at most number of distinct digit sums)

### 2. Optimal — Python

Recommendedpython

```python

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = [0] * 50

        for num in range(lowLimit, highLimit + 1):
            x = num
            total = 0

            while x > 0:
                total += x % 10
                x //= 10

            boxes[total] += 1

        return max(boxes)
```

- Time Complexity: O(N × D)
- Space Complexity: O(1) (fixed-size array)
