# You are given a 0-indexed integer array nums and an integer k.

# You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

# You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

# Return the maximum score you can get.



# Example 1:

# Input: nums = [1,-1,-2,4,-7,3], k = 2
# Output: 7
# Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
# Example 2:

# Input: nums = [10,-5,-2,4,0,3], k = 3
# Output: 17
# Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
# Example 3:

# Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# Output: 0


# Constraints:

# 1 <= nums.length, k <= 105
# -104 <= nums[i] <= 104
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
# ### 1. Brute Force Approach (Dynamic Programming)

python

```python

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [float('-inf')] * n

        dp[0] = nums[0]

        for i in range(1, n):
            for j in range(max(0, i - k), i):
                dp[i] = max(dp[i], dp[j] + nums[i])

        return dp[n - 1]
```

Time Complexity: O(n \* k)

Space Complexity: O(n)

### 2. Optimal Approach (Monotonic Deque + DP)

Optimalpython

```python

from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]
        dq = deque([0])

        for i in range(1, n):
            while dq and dq[0] < i - k:
                dq.popleft()

            dp[i] = nums[i] + dp[dq[0]]

            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            dq.append(i)

        return dp[n - 1]
```

Time Complexity: O(n)

Space Complexity: O(n)
