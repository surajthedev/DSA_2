# Given 2n balls of k distinct colors. You will be given an integer array balls of size k where balls[i] is the number of balls of color i.

# All the balls will be shuffled uniformly at random, then we will distribute the first n balls to the first box and the remaining n balls to the other box (Please read the explanation of the second example carefully).

# Please note that the two boxes are considered different. For example, if we have two balls of colors a and b, and two boxes [] and (), then the distribution [a] (b) is considered different than the distribution [b] (a) (Please read the explanation of the first example carefully).

# Return the probability that the two boxes have the same number of distinct balls. Answers within 10-5 of the actual value will be accepted as correct.



# Example 1:

# Input: balls = [1,1]
# Output: 1.00000
# Explanation: Only 2 ways to divide the balls equally:
# - A ball of color 1 to box 1 and a ball of color 2 to box 2
# - A ball of color 2 to box 1 and a ball of color 1 to box 2
# In both ways, the number of distinct colors in each box is equal. The probability is 2/2 = 1
# Example 2:

# Input: balls = [2,1,1]
# Output: 0.66667
# Explanation: We have the set of balls [1, 1, 2, 3]
# This set of balls will be shuffled randomly and we may have one of the 12 distinct shuffles with equal probability (i.e. 1/12):
# [1,1 / 2,3], [1,1 / 3,2], [1,2 / 1,3], [1,2 / 3,1], [1,3 / 1,2], [1,3 / 2,1], [2,1 / 1,3], [2,1 / 3,1], [2,3 / 1,1], [3,1 / 1,2], [3,1 / 2,1], [3,2 / 1,1]
# After that, we add the first two balls to the first box and the second two balls to the second box.
# We can see that 8 of these 12 possible random distributions have the same number of distinct colors of balls in each box.
# Probability is 8/12 = 0.66667
# Example 3:

# Input: balls = [1,2,1,2]
# Output: 0.60000
# Explanation: The set of balls is [1, 2, 2, 3, 4, 4]. It is hard to display all the 180 possible random shuffles of this set but it is easy to check that 108 of them will have the same number of distinct colors in each box.
# Probability = 108 / 180 = 0.6


# Constraints:

# 1 <= balls.length <= 8
# 1 <= balls[i] <= 6
# sum(balls) is even.
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
# ## 1. Brute Force Solution (Backtracking)

python

```python
from typing import List
from math import comb

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls) // 2
        total = 0
        valid = 0

        def dfs(i, count1, distinct1, distinct2, ways):
            nonlocal total, valid

            if i == len(balls):
                if count1 == n:
                    total += ways
                    if distinct1 == distinct2:
                        valid += ways
                return

            for x in range(balls[i] + 1):
                y = balls[i] - x

                if count1 + x <= n:
                    dfs(
                        i + 1,
                        count1 + x,
                        distinct1 + (x > 0),
                        distinct2 + (y > 0),
                        ways * comb(balls[i], x)
                    )

        dfs(0, 0, 0, 0, 1)

        return valid / total
```

## 2. Optimal Solution (Dynamic Programming + Memoization)

python

```python
from typing import List
from functools import lru_cache
from math import comb

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls) // 2
        k = len(balls)

        @lru_cache(None)
        def dp(i, count1, diff):
            if count1 > n or count1 + sum(balls[i:]) < n:
                return 0.0

            if i == k:
                return 1.0 if count1 == n and diff == 0 else 0.0

            ans = 0.0

            for x in range(balls[i] + 1):
                y = balls[i] - x

                ans += comb(balls[i], x) * dp(
                    i + 1,
                    count1 + x,
                    diff + (x > 0) - (y > 0)
                )

            return ans

        numerator = dp(0, 0, 0)
        denominator = comb(sum(balls), n)

        return numerator / denominator
```

Time: O(k × n × D × max(balls\[i\]))Space: O(k × n × D)
