# You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

# You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

# Return the maximum sum of values that you can receive by attending events.



# Example 1:



# Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
# Output: 7
# Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
# Example 2:



# Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
# Output: 10
# Explanation: Choose event 2 for a total value of 10.
# Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
# Example 3:



# Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
# Output: 9
# Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.


# Constraints:

# 1 <= k <= events.length
# 1 <= k * events.length <= 106
# 1 <= startDayi <= endDayi <= 109
# 1 <= valuei <= 106
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
# ### Brute Force (Recursive + Memoization)

python

```python
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        from functools import lru_cache

        events.sort()

        n = len(events)

        @lru_cache(None)
        def solve(index, count):
            if index == n or count == 0:
                return 0

            skip = solve(index + 1, count)

            next_index = index + 1
            while next_index < n and events[next_index][0] <= events[index][1]:
                next_index += 1

            take = events[index][2] + solve(next_index, count - 1)

            return max(take, skip)

        return solve(0, k)
```

### Optimal (DP + Binary Search)

python

```python
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        from bisect import bisect_right

        events.sort()

        n = len(events)
        starts = [event[0] for event in events]

        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            next_index = bisect_right(starts, events[i][1])

            for j in range(1, k + 1):
                take = events[i][2] + dp[next_index][j - 1]
                skip = dp[i + 1][j]

                dp[i][j] = max(take, skip)

        return dp[0][k]
```
