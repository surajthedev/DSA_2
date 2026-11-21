# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.



# Example 1:

# Input: nums = [1,3,1]
# Output: 0
# Explanation: The array itself is a mountain array so we do not need to remove any elements.
# Example 2:

# Input: nums = [2,1,1,5,6,2,3,1]
# Output: 3
# Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].


# Constraints:

# 3 <= nums.length <= 1000
# 1 <= nums[i] <= 109
# It is guaranteed that you can make a mountain array out of nums.
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
# ### 1. Brute Force Approach (LIS + LDS)

Time: O(N³) — Space: O(N)python

```python
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        lis = [1] * n
        lds = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], lds[j] + 1)

        ans = n

        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:
                ans = min(ans, n - (lis[i] + lds[i] - 1))

        return ans
```

### 2. Optimal Approach (Binary Search + LIS)

Time: O(N log N) — Space: O(N)python

```python
from bisect import bisect_left

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        lis = [0] * n
        lds = [0] * n

        tails = []

        for i in range(n):
            pos = bisect_left(tails, nums[i])

            if pos == len(tails):
                tails.append(nums[i])
            else:
                tails[pos] = nums[i]

            lis[i] = pos + 1

        tails = []

        for i in range(n - 1, -1, -1):
            pos = bisect_left(tails, nums[i])

            if pos == len(tails):
                tails.append(nums[i])
            else:
                tails[pos] = nums[i]

            lds[i] = pos + 1

        ans = n

        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:
                mountain = lis[i] + lds[i] - 1
                ans = min(ans, n - mountain)

        return ans
```
