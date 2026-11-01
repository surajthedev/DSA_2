# You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

# Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

# The performance of a team is the sum of its engineers' speeds multiplied by the minimum efficiency among its engineers.

# Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.



# Example 1:

# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
# Output: 60
# Explanation:
# We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
# Example 2:

# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
# Output: 68
# Explanation:
# This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
# Example 3:

# Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
# Output: 72


# Constraints:

# 1 <= k <= n <= 105
# speed.length == n
# efficiency.length == n
# 1 <= speed[i] <= 105
# 1 <= efficiency[i] <= 108
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
# ### Brute Force Approach

python

```python
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        import itertools

        MOD = 10**9 + 7
        ans = 0

        for size in range(1, k + 1):
            for team in itertools.combinations(range(n), size):
                total_speed = sum(speed[i] for i in team)
                min_eff = min(efficiency[i] for i in team)

                performance = total_speed * min_eff
                ans = max(ans, performance)

        return ans % MOD
```

### Optimal Approach (Greedy + Max Heap)

python

```python
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        import heapq

        MOD = 10**9 + 7

        engineers = sorted(zip(efficiency, speed), reverse=True)

        min_heap = []
        total_speed = 0
        ans = 0

        for eff, spd in engineers:
            heapq.heappush(min_heap, spd)
            total_speed += spd

            if len(min_heap) > k:
                total_speed -= heapq.heappop(min_heap)

            performance = total_speed * eff
            ans = max(ans, performance)

        return ans % MOD
```
