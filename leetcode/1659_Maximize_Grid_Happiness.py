# You are given four integers, m, n, introvertsCount, and extrovertsCount. You have an m x n grid, and there are two types of people: introverts and extroverts. There are introvertsCount introverts and extrovertsCount extroverts.

# You should decide how many people you want to live in the grid and assign each of them one grid cell. Note that you do not have to have all the people living in the grid.

# The happiness of each person is calculated as follows:

# Introverts start with 120 happiness and lose 30 happiness for each neighbor (introvert or extrovert).
# Extroverts start with 40 happiness and gain 20 happiness for each neighbor (introvert or extrovert).
# Neighbors live in the directly adjacent cells north, east, south, and west of a person's cell.

# The grid happiness is the sum of each person's happiness. Return the maximum possible grid happiness.



# Example 1:


# Input: m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
# Output: 240
# Explanation: Assume the grid is 1-indexed with coordinates (row, column).
# We can put the introvert in cell (1,1) and put the extroverts in cells (1,3) and (2,3).
# - Introvert at (1,1) happiness: 120 (starting happiness) - (0 * 30) (0 neighbors) = 120
# - Extrovert at (1,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
# - Extrovert at (2,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
# The grid happiness is 120 + 60 + 60 = 240.
# The above figure shows the grid in this example with each person's happiness. The introvert stays in the light green cell while the extroverts live on the light purple cells.
# Example 2:

# Input: m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
# Output: 260
# Explanation: Place the two introverts in (1,1) and (3,1) and the extrovert at (2,1).
# - Introvert at (1,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
# - Extrovert at (2,1) happiness: 40 (starting happiness) + (2 * 20) (2 neighbors) = 80
# - Introvert at (3,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
# The grid happiness is 90 + 80 + 90 = 260.
# Example 3:

# Input: m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
# Output: 240


# Constraints:

# 1 <= m, n <= 5
# 0 <= introvertsCount, extrovertsCount <= min(m * n, 6)
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
# ### Brute Force — Backtracking

python

```python
from functools import lru_cache
from typing import List

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        grid = [0] * (m * n)
        ans = 0

        def backtrack(pos, intro, extro, happiness):
            nonlocal ans

            if pos == m * n:
                ans = max(ans, happiness)
                return

            backtrack(pos + 1, intro, extro, happiness)

            if intro > 0:
                gain = 120
                for neighbor in (pos - n, pos - 1):
                    if neighbor >= 0:
                        if neighbor == pos - 1 and pos % n == 0:
                            continue
                        if grid[neighbor] == 1:
                            gain -= 60
                        elif grid[neighbor] == 2:
                            gain -= 10

                grid[pos] = 1
                backtrack(pos + 1, intro - 1, extro, happiness + gain)
                grid[pos] = 0

            if extro > 0:
                gain = 40
                for neighbor in (pos - n, pos - 1):
                    if neighbor >= 0:
                        if neighbor == pos - 1 and pos % n == 0:
                            continue
                        if grid[neighbor] == 1:
                            gain -= 10
                        elif grid[neighbor] == 2:
                            gain += 40

                grid[pos] = 2
                backtrack(pos + 1, intro, extro - 1, happiness + gain)
                grid[pos] = 0

        backtrack(0, introvertsCount, extrovertsCount, 0)
        return ans
```

### Optimal Approach — Bitmask DP (Memoization)

python

```python
from functools import lru_cache

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:

        @lru_cache(None)
        def dp(pos, intro, extro, mask):
            if pos == m * n:
                return 0

            ans = dp(pos + 1, intro, extro, (mask << 2) & ((1 << (2 * n)) - 1))

            up = (mask >> (2 * (n - 1))) & 3
            left = mask & 3 if pos % n else 0

            for person in (1, 2):
                if person == 1 and intro == 0:
                    continue
                if person == 2 and extro == 0:
                    continue

                base = 120 if person == 1 else 40

                if up:
                    base += self_effect(person, up)

                if left:
                    base += self_effect(person, left)

                new_mask = ((mask << 2) | person) & ((1 << (2 * n)) - 1)

                value = dp(
                    pos + 1,
                    intro - (person == 1),
                    extro - (person == 2),
                    new_mask
                )

                ans = max(ans, base + value)

            return ans

        return dp(0, introvertsCount, extrovertsCount, 0)


def self_effect(a, b):
    happiness = {1: -30, 2: 20}
    return happiness[a] + happiness[b]
```s
