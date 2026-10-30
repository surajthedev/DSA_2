# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

# You can attend an event i at any day d where startDayi <= d <= endDayi. You can only attend one event at any time d.

# Return the maximum number of events you can attend.



# Example 1:


# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3
# Explanation: You can attend all the three events.
# One way to attend them all is as shown.
# Attend the first event on day 1.
# Attend the second event on day 2.
# Attend the third event on day 3.
# Example 2:

# Input: events= [[1,2],[2,3],[3,4],[1,2]]
# Output: 4


# Constraints:

# 1 <= events.length <= 105
# events[i].length == 2
# 1 <= startDayi <= endDayi <= 105
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
# ### 1. Brute Force – Greedy (O(n²))

python

```
class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort()
        attended = set()

        count = 0

        for start, end in events:
            for day in range(start, end + 1):
                if day not in attended:
                    attended.add(day)
                    count += 1
                    break

        return count
```

### 2. Optimal – Min Heap + Greedy (O(n log n))

python

```
import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort()

        heap = []
        n = len(events)
        i = 0
        day = 0
        count = 0

        while i < n or heap:
            if not heap:
                day = max(day, events[i][0])

            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1

            while heap and heap[0] < day:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                count += 1
                day += 1

        return count
```
