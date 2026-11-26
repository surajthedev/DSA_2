# You are given an integer array nums and an integer goal.

# You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).

# Return the minimum possible value of abs(sum - goal).

# Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.



# Example 1:

# Input: nums = [5,-7,3,5], goal = 6
# Output: 0
# Explanation: Choose the whole array as a subsequence, with a sum of 6.
# This is equal to the goal, so the absolute difference is 0.
# Example 2:

# Input: nums = [7,-9,15,-2], goal = -5
# Output: 1
# Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
# The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.
# Example 3:

# Input: nums = [1,2,3], goal = -7
# Output: 7


# Constraints:

# 1 <= nums.length <= 40
# -107 <= nums[i] <= 107
# -109 <= goal <= 109
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
# ### Brute Force (All Subsequences)

python

```python
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        from itertools import combinations

        sums = [0]

        for num in nums:
            sums += [x + num for x in sums]

        return min(abs(x - goal) for x in sums)
```

### Optimal (Meet in the Middle + Binary Search)

python

```python
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        from bisect import bisect_left

        def get_sums(arr):
            sums = [0]

            for num in arr:
                sums += [x + num for x in sums]

            return sums

        mid = len(nums) // 2

        left = get_sums(nums[:mid])
        right = sorted(get_sums(nums[mid:]))

        ans = abs(goal)

        for x in left:
            target = goal - x
            i = bisect_left(right, target)

            if i < len(right):
                ans = min(ans, abs(x + right[i] - goal))

            if i > 0:
                ans = min(ans, abs(x + right[i - 1] - goal))

            if ans == 0:
                return 0

        return ans
```
