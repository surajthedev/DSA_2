# You are given an array nums of n integers and an integer k.

# For each subarray of nums, you can apply up to k operations on it. In each operation, you increment any element of the subarray by 1.

# Note that each subarray is considered independently, meaning changes made to one subarray do not persist to another.

# Return the number of subarrays that you can make non-decreasing ​​​​​after performing at most k operations.

# An array is said to be non-decreasing if each element is greater than or equal to its previous element, if it exists.



# Example 1:

# Input: nums = [6,3,1,2,4,4], k = 7

# Output: 17

# Explanation:

# Out of all 21 possible subarrays of nums, only the subarrays [6, 3, 1], [6, 3, 1, 2], [6, 3, 1, 2, 4] and [6, 3, 1, 2, 4, 4] cannot be made non-decreasing after applying up to k = 7 operations. Thus, the number of non-decreasing subarrays is 21 - 4 = 17.

# Example 2:

# Input: nums = [6,3,1,3,6], k = 4

# Output: 12

# Explanation:

# The subarray [3, 1, 3, 6] along with all subarrays of nums with three or fewer elements, except [6, 3, 1], can be made non-decreasing after k operations. There are 5 subarrays of a single element, 4 subarrays of two elements, and 2 subarrays of three elements except [6, 3, 1], so there are 1 + 5 + 4 + 2 = 12 subarrays that can be made non-decreasing.



# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109
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
#**Brute Force (O(n²))**
```python
class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        ans = 0
        for l in range(n):
            cost = 0
            mx = nums[l]
            for r in range(l, n):
                mx = max(mx, nums[r])
                cost += mx - nums[r]
                if cost > k:
                    break
                ans += 1
        return ans
```

**Optimal (O(n))**
```python
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        dq = deque()      # [value, count] segments, front = left side
        S = 0             # sum of value*count over segments
        W = 0             # sum of nums[l..r]
        r = n - 1
        ans = 0
        for l in range(n - 1, -1, -1):
            cnt = 1
            while dq and dq[0][0] <= nums[l]:
                v, c = dq.popleft()
                S -= v * c
                cnt += c
            dq.appendleft([nums[l], cnt])
            S += nums[l] * cnt
            W += nums[l]
            while S - W > k:
                W -= nums[r]
                dq[-1][1] -= 1
                S -= dq[-1][0]
                if dq[-1][1] == 0:
                    dq.pop()
                r -= 1
            ans += r - l + 1
        return ans
```
