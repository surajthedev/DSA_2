# You are given an integer array nums and two integers, x and k. You can perform the following operation any number of times (including zero):

# Increase or decrease any element of nums by 1.
# Return the minimum number of operations needed to have at least k non-overlapping subarrays of size exactly x in nums, where all elements within each subarray are equal.



# Example 1:

# Input: nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2

# Output: 8

# Explanation:

# Use 3 operations to add 3 to nums[1] and use 2 operations to subtract 2 from nums[3]. The resulting array is [5, 1, 1, 1, 7, 3, 6, 4, -1].
# Use 1 operation to add 1 to nums[5] and use 2 operations to subtract 2 from nums[6]. The resulting array is [5, 1, 1, 1, 7, 4, 4, 4, -1].
# Now, all elements within each subarray [1, 1, 1] (from indices 1 to 3) and [4, 4, 4] (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.
# Example 2:

# Input: nums = [9,-2,-2,-2,1,5], x = 2, k = 2

# Output: 3

# Explanation:

# Use 3 operations to subtract 3 from nums[4]. The resulting array is [9, -2, -2, -2, -2, 5].
# Now, all elements within each subarray [-2, -2] (from indices 1 to 2) and [-2, -2] (from indices 3 to 4) are equal. Since 3 operations were used, 3 is the output.


# Constraints:

# 2 <= nums.length <= 105
# -106 <= nums[i] <= 106
# 2 <= x <= nums.length
# 1 <= k <= 15
# 2 <= k * x <= nums.length
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
# ### Brute Force (DP + Median)

python

```python
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        INF = float('inf')

        cost = [0] * (n - x + 1)

        for i in range(n - x + 1):
            arr = sorted(nums[i:i + x])
            median = arr[x // 2]
            cost[i] = sum(abs(v - median) for v in arr)

        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(k + 1):
                dp[i][j] = dp[i - 1][j]

                if j > 0 and i >= x:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - x][j - 1] + cost[i - x]
                    )

        return dp[n][k]
```




# Optimal:
import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        m = n - x + 1

        # ---- sliding window cost (sum of abs deviations from median) ----
        lo, hi = [], []          # lo: max-heap (neg), hi: min-heap
        delayed = {}
        lo_size = hi_size = 0
        lo_sum = hi_sum = 0

        def prune(heap, is_lo):
            while heap:
                v = -heap[0] if is_lo else heap[0]
                if delayed.get(v, 0) > 0:
                    delayed[v] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            nonlocal lo_size, hi_size, lo_sum, hi_sum
            if lo_size > hi_size + 1:
                v = -heapq.heappop(lo)
                heapq.heappush(hi, v)
                lo_size -= 1; hi_size += 1
                lo_sum -= v; hi_sum += v
                prune(lo, True)
            elif lo_size < hi_size:
                v = heapq.heappop(hi)
                heapq.heappush(lo, -v)
                hi_size -= 1; lo_size += 1
                hi_sum -= v; lo_sum += v
                prune(hi, False)

        def add(v):
            nonlocal lo_size, hi_size, lo_sum, hi_sum
            if not lo or v <= -lo[0]:
                heapq.heappush(lo, -v); lo_size += 1; lo_sum += v
            else:
                heapq.heappush(hi, v); hi_size += 1; hi_sum += v
            balance()

        def remove(v):
            nonlocal lo_size, hi_size, lo_sum, hi_sum
            delayed[v] = delayed.get(v, 0) + 1
            if v <= -lo[0]:
                lo_size -= 1; lo_sum -= v
                if v == -lo[0]:
                    prune(lo, True)
            else:
                hi_size -= 1; hi_sum -= v
                if hi and v == hi[0]:
                    prune(hi, False)
            balance()

        costs = [0] * m
        for i in range(n):
            add(nums[i])
            if i >= x:
                remove(nums[i - x])
            if i >= x - 1:
                med = -lo[0]
                costs[i - x + 1] = (med * lo_size - lo_sum) + (hi_sum - med * hi_size)

        # ---- DP: dp[j][i] = min cost using j subarrays from windows starting at >= i ----
        INF = float('inf')
        prev = [0] * (n + 1)     # j = 0
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(n - 1, -1, -1):
                best = cur[i + 1]
                if i < m and i + x <= n:
                    best = min(best, costs[i] + prev[i + x])
                cur[i] = best
            prev = cur

        return prev[0]
