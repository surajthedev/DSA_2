# A split of an integer array is good if:

# The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
# The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
# Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.



# Example 1:

# Input: nums = [1,1,1]
# Output: 1
# Explanation: The only good way to split nums is [1] [1] [1].
# Example 2:

# Input: nums = [1,2,2,2,5,0]
# Output: 3
# Explanation: There are three good ways of splitting nums:
# [1] [2] [2,2,5,0]
# [1] [2,2] [2,5,0]
# [1,2] [2,2] [5,0]
# Example 3:

# Input: nums = [3,2,1]
# Output: 0
# Explanation: There is no good way to split nums.


# Constraints:

# 3 <= nums.length <= 105
# 0 <= nums[i] <= 104
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
#
# ### 1. Brute Force Approach

python

```python
from typing import List

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        ans = 0

        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                left = prefix[i]
                mid = prefix[j] - prefix[i]
                right = prefix[n - 1] - prefix[j]

                if left <= mid <= right:
                    ans += 1

        return ans % MOD
```

Time Complexity: $O(n^2)$

Space Complexity: $O(n)$

### 2. Optimal Approach (Binary Search)

python

```python
from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = 0
        total = prefix[n]

        for i in range(1, n - 1):
            left = prefix[i]

            low = bisect_left(prefix, 2 * left, i + 1, n)
            high = bisect_right(
                prefix,
                (total + left) // 2,
                low,
                n
            ) - 1

            ans += max(0, high - low + 1)

        return ans % MOD
```

Time Complexity: $O(n \log n)$

Space Complexity: $O(n)$
