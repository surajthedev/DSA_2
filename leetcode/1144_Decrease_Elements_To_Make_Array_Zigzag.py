# Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

# An array A is a zigzag array if either:

# Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
# OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
# Return the minimum number of moves to transform the given array nums into a zigzag array.



# Example 1:

# Input: nums = [1,2,3]
# Output: 2
# Explanation: We can decrease 2 to 0 or 3 to 1.
# Example 2:

# Input: nums = [9,6,1,6,2]
# Output: 4


# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
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
# ### Brute Force — O(n²)

python
```
from typing import List

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')

        for peak in (0, 1):
            arr = nums[:]
            moves = 0

            for i in range(n):
                if i % 2 == peak:
                    continue

                left = arr[i - 1] if i > 0 else float('inf')
                right = arr[i + 1] if i < n - 1 else float('inf')
                target = min(left, right) - 1

                if arr[i] > target:
                    moves += arr[i] - target

            ans = min(ans, moves)

        return ans
```

### Optimal — O(n) Time, O(1) Space

python
```
from typing import List

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [0, 0]

        for i in range(n):
            left = nums[i - 1] if i > 0 else float('inf')
            right = nums[i + 1] if i < n - 1 else float('inf')

            decrease = max(0, nums[i] - min(left, right) + 1)

            ans[i % 2] += decrease

        return min(ans)
```
