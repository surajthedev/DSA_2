# You are given an array of integers nums and an integer limit.

# Return the size of the longest non-empty subarray such that the absolute difference between every pair of elements in this subarray is less than or equal to limit.



# Example 1:

# Input: nums = [8,2,4,7], limit = 4

# Output: 2

# Explanation:

# Checking every subarray, where the absolute difference is taken over all pairs of its elements:
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |4-2| = 2 <= 4.
# [2,4,7] with maximum absolute diff |7-2| = 5 > 4. Note that the pair (2, 7) is not adjacent, but it is still compared.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |7-4| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4.
# Therefore, the size of the longest subarray is 2.

# Example 2:

# Input: nums = [10,1,2,4,7,2], limit = 5

# Output: 4

# Explanation:

# The subarray [2,4,7,2] is valid because every pair of its elements differs by at most 5, the largest being |7-2| = 5.

# It cannot be extended to the left, since [1,2,4,7,2] contains the pair (1, 7) with |7-1| = 6 > 5. Therefore, the size of the longest subarray is 4.

# Example 3:

# Input: nums = [4,2,2,2,4,4,2,2], limit = 0

# Output: 3

# Explanation:

# Since limit = 0, every pair of elements in the subarray must be equal, so only runs of identical values qualify.

# The longest such run is [2,2,2], of size 3.



# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 0 <= limit <= 109
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
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            mini = float('inf')
            maxi = float('-inf')

            for j in range(i, n):
                mini = min(mini, nums[j])
                maxi = max(maxi, nums[j])

                if maxi - mini <= limit:
                    ans = max(ans, j - i + 1)
                else:
                    break

        return ans
```

Time Complexity: O(n²)

Space Complexity: O(1)

### 2. Optimal Approach — Sliding Window + Monotonic Deque

python

```python
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_dq = deque()
        max_dq = deque()

        left = 0
        ans = 0

        for right in range(len(nums)):

            while min_dq and nums[min_dq[-1]] > nums[right]:
                min_dq.pop()

            min_dq.append(right)

            while max_dq and nums[max_dq[-1]] < nums[right]:
                max_dq.pop()

            max_dq.append(right)

            while nums[max_dq[0]] - nums[min_dq[0]] > limit:

                if min_dq[0] == left:
                    min_dq.popleft()

                if max_dq[0] == left:
                    max_dq.popleft()

                left += 1

            ans = max(ans, right - left + 1)

        return ans
```

Time Complexity: O(n)

Space Complexity: O(n)
