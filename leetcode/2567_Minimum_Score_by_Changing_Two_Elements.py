# You are given an integer array nums.

# The low score of nums is the minimum absolute difference between any two integers.
# The high score of nums is the maximum absolute difference between any two integers.
# The score of nums is the sum of the high and low scores.
# Return the minimum score after changing two elements of nums.



# Example 1:

# Input: nums = [1,4,7,8,5]

# Output: 3

# Explanation:

# Change nums[0] and nums[1] to be 6 so that nums becomes [6,6,7,8,5].
# The low score is the minimum absolute difference: |6 - 6| = 0.
# The high score is the maximum absolute difference: |8 - 5| = 3.
# The sum of high and low score is 3.
# Example 2:

# Input: nums = [1,4,3]

# Output: 0

# Explanation:

# Change nums[1] and nums[2] to 1 so that nums becomes [1,1,1].
# The sum of maximum absolute difference and minimum absolute difference is 0.


# Constraints:

# 3 <= nums.length <= 105
# 1 <= nums[i] <= 109
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
# Sorry\! Correct LeetCode function name `minimizeSum` hai. Is question mein 2 elements change karne hain, isliye sorted array ke 4 possible cases check honge.

### Brute Force (TLE possible)

python

```python
from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')

        for i in range(n):
            for j in range(i + 1, n):
                arr = nums[:]
                arr[i] = arr[j]
                arr.sort()

                score = arr[-1] - arr[0]
                ans = min(ans, score)

        return ans
```

### Optimal Solution (Accepted)

python

```python
from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        return min(
            nums[n-1] - nums[2],
            nums[n-2] - nums[1],
            nums[n-3] - nums[0]
        )
```
