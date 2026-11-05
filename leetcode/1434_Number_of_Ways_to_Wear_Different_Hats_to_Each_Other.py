# There are n people and 40 types of hats labeled from 1 to 40.

# Given a 2D integer array hats, where hats[i] is a list of all hats preferred by the ith person.

# Return the number of ways that n people can wear different hats from each other.

# Since the answer may be too large, return it modulo 109 + 7.



# Example 1:

# Input: hats = [[3,4],[4,5],[5]]
# Output: 1
# Explanation: There is only one way to choose hats given the conditions.
# First person chooses hat 3, Second person chooses hat 4 and last one hat 5.
# Example 2:

# Input: hats = [[3,5,1],[3,5]]
# Output: 4
# Explanation: There are 4 ways to choose hats:
# (3,5), (5,3), (1,3) and (1,5)
# Example 3:

# Input: hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# Output: 24
# Explanation: Each person can choose hats labeled from 1 to 4.
# Number of Permutations of (1,2,3,4) = 24.


# Constraints:

# n == hats.length
# 1 <= n <= 10
# 1 <= hats[i].length <= 40
# 1 <= hats[i][j] <= 40
# hats[i] contains a list of unique integers.
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
# ### 1. Brute Force Approach — Backtracking

python

```python
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(hats)
        ans = 0

        def backtrack(person, used):
            nonlocal ans

            if person == n:
                ans += 1
                return

            for hat in hats[person]:
                if hat not in used:
                    used.add(hat)
                    backtrack(person + 1, used)
                    used.remove(hat)

        backtrack(0, set())

        return ans % MOD
```

Time Complexity: O(40^n × n)

Space Complexity: O(n + 40)

### 2. Optimal Approach — Bitmask DP

python

```python
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(hats)

        hat_to_people = [[] for _ in range(41)]

        for person in range(n):
            for hat in hats[person]:
                hat_to_people[hat].append(person)

        dp = [0] * (1 << n)
        dp[0] = 1

        for hat in range(1, 41):
            new_dp = dp[:]

            for mask in range(1 << n):
                if dp[mask] == 0:
                    continue

                for person in hat_to_people[hat]:
                    if not (mask & (1 << person)):
                        new_mask = mask | (1 << person)

                        new_dp[new_mask] = (
                            new_dp[new_mask] + dp[mask]
                        ) % MOD

            dp = new_dp

        return dp[(1 << n) - 1]
```

Time Complexity: O(40 × 2^n × n)

Space Complexity: O(2^n + 40n)
