# You are given an array nums​​​ and an integer k​​​​​. The XOR of a segment [left, right] where left <= right is the XOR of all the elements with indices between left and right, inclusive: nums[left] XOR nums[left+1] XOR ... XOR nums[right].

# Return the minimum number of elements to change in the array such that the XOR of all segments of size k​​​​​​ is equal to zero.



# Example 1:

# Input: nums = [1,2,0,3,0], k = 1
# Output: 3
# Explanation: Modify the array from [1,2,0,3,0] to from [0,0,0,0,0].
# Example 2:

# Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
# Output: 3
# Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to [3,4,7,3,4,7,3,4,7].
# Example 3:

# Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
# Output: 3
# Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to [1,2,3,1,2,3,1,2,3].


# Constraints:

# 1 <= k <= nums.length <= 2000
# ​​​​​​0 <= nums[i] < 210
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
# ### 1. Brute Force — DP (O(k × 1024²))

python

```python
from collections import Counter

class Solution:
    def minChanges(self, nums, k):
        n = len(nums)
        MAX = 1024
        INF = float('inf')

        dp = [INF] * MAX
        dp[0] = 0

        for i in range(k):
            freq = Counter(nums[i::k])
            size = len(nums[i::k])

            ndp = [INF] * MAX

            for prev in range(MAX):
                if dp[prev] == INF:
                    continue

                for val in range(MAX):
                    cost = size - freq.get(val, 0)
                    x = prev ^ val

                    ndp[x] = min(ndp[x], dp[prev] + cost)

            dp = ndp

        return dp[0]
```

### 2. Optimal — DP + XOR (O(n × 1024))

python

```python
from collections import Counter

class Solution:
    def minChanges(self, nums, k):
        MAX = 1024
        INF = float('inf')
        n = len(nums)

        dp = [INF] * MAX
        dp[0] = 0

        for i in range(k):
            freq = Counter(nums[i::k])
            size = len(nums[i::k])

            mn = min(dp)
            ndp = [mn + size] * MAX

            for prev in range(MAX):
                for val, count in freq.items():
                    x = prev ^ val

                    ndp[x] = min(
                        ndp[x],
                        dp[prev] + size - count
                    )

            dp = ndp

        return dp[0]
```
