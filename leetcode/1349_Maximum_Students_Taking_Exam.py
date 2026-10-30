# Given a m * n matrix seats  that represent seats distributions in a classroom. If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.

# Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the maximum number of students that can take the exam together without any cheating being possible.

# Students must be placed in seats in good condition.



# Example 1:


# Input: seats = [["#",".","#","#",".","#"],
#                 [".","#","#","#","#","."],
#                 ["#",".","#","#",".","#"]]
# Output: 4
# Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam.
# Example 2:

# Input: seats = [[".","#"],
#                 ["#","#"],
#                 ["#","."],
#                 ["#","#"],
#                 [".","#"]]
# Output: 3
# Explanation: Place all students in available seats.

# Example 3:

# Input: seats = [["#",".",".",".","#"],
#                 [".","#",".","#","."],
#                 [".",".","#",".","."],
#                 [".","#",".","#","."],
#                 ["#",".",".",".","#"]]
# Output: 10
# Explanation: Place students in available seats in column 1, 3 and 5.


# Constraints:

# seats contains only characters '.' and'#'.
# m == seats.length
# n == seats[i].length
# 1 <= m <= 8
# 1 <= n <= 8
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
# ### 1. Brute Force – Backtracking

python

```
class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        m, n = len(seats), len(seats[0])
        ans = 0

        def backtrack(pos, occupied, count):
            nonlocal ans

            if pos == m * n:
                ans = max(ans, count)
                return

            r, c = divmod(pos, n)

            backtrack(pos + 1, occupied, count)

            if seats[r][c] == '#':
                return

            valid = True

            for dr, dc in [(0, -1), (0, 1), (-1, -1), (-1, 1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    idx = nr * n + nc

                    if occupied & (1 << idx):
                        valid = False
                        break

            if valid:
                backtrack(
                    pos + 1,
                    occupied | (1 << pos),
                    count + 1
                )

        backtrack(0, 0, 0)
        return ans
```

### 2. Optimal – Bitmask DP

python

```
class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        m, n = len(seats), len(seats[0])

        valid_masks = []

        for r in range(m):
            mask = 0

            for c in range(n):
                if seats[r][c] == '.':
                    mask |= (1 << c)

            valid_masks.append(mask)

        dp = {}

        for mask in range(1 << n):
            if mask & (mask << 1):
                continue

            if mask & ~valid_masks[0]:
                continue

            dp[mask] = bin(mask).count('1')

        for r in range(1, m):
            new_dp = {}

            for mask in range(1 << n):
                if mask & (mask << 1):
                    continue

                if mask & ~valid_masks[r]:
                    continue

                count = bin(mask).count('1')
                best = 0

                for prev in dp:
                    if (mask & (prev << 1)) or (mask & (prev >> 1)):
                        continue

                    best = max(best, dp[prev])

                new_dp[mask] = best + count

            dp = new_dp

        return max(dp.values())
```
