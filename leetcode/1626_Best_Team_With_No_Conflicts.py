# You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

# However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

# Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.



# Example 1:

# Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
# Output: 34
# Explanation: You can choose all the players.
# Example 2:

# Input: scores = [4,5,6,5], ages = [2,1,2,1]
# Output: 16
# Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
# Example 3:

# Input: scores = [1,2,3,5], ages = [8,9,10,1]
# Output: 6
# Explanation: It is best to choose the first 3 players.


# Constraints:

# 1 <= scores.length, ages.length <= 1000
# scores.length == ages.length
# 1 <= scores[i] <= 106
# 1 <= ages[i] <= 1000
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
# ### 1. Brute Force Approach (DP)

python

```python
from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))
        n = len(players)

        dp = [0] * n
        ans = 0

        for i in range(n):
            dp[i] = players[i][1]

            for j in range(i):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])

            ans = max(ans, dp[i])

        return ans
```

### 2. Optimal Approach (Sorting + Fenwick Tree / BIT)

python

```python
from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))
        max_score = max(scores)

        bit = [0] * (max_score + 2)

        def query(i):
            res = 0
            while i > 0:
                res = max(res, bit[i])
                i -= i & -i
            return res

        def update(i, val):
            while i <= max_score:
                bit[i] = max(bit[i], val)
                i += i & -i

        ans = 0

        for age, score in players:
            curr = query(score) + score
            update(score, curr)
            ans = max(ans, curr)

        return ans
```
