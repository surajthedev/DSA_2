# You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [0..n - 1].

# You may swap elements at indices i and j only if nums[i] AND nums[j] == k, where AND denotes the bitwise AND operation and k is a non-negative integer.

# Return the maximum value of k such that the array can be sorted in non-decreasing order using any number of such swaps. If nums is already sorted, return 0.



# Example 1:

# Input: nums = [0,3,2,1]

# Output: 1

# Explanation:

# Choose k = 1. Swapping nums[1] = 3 and nums[3] = 1 is allowed since nums[1] AND nums[3] == 1, resulting in a sorted permutation: [0, 1, 2, 3].

# Example 2:

# Input: nums = [0,1,3,2]

# Output: 2

# Explanation:

# Choose k = 2. Swapping nums[2] = 3 and nums[3] = 2 is allowed since nums[2] AND nums[3] == 2, resulting in a sorted permutation: [0, 1, 2, 3].

# Example 3:

# Input: nums = [3,2,1,0]

# Output: 0

# Explanation:

# Only k = 0 allows sorting since no greater k allows the required swaps where nums[i] AND nums[j] == k.



# Constraints:

# 1 <= n == nums.length <= 105
# 0 <= nums[i] <= n - 1
# nums is a permutation of integers from 0 to n - 1.
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
# python
```
# Brute Force
class Solution:
    def sortArray(self, nums: list[int]) -> int:
        n = len(nums)

        if nums == sorted(nums):
            return 0

        for k in range(n - 1, 0, -1):
            arr = nums[:]

            changed = True
            while changed:
                changed = False
                for i in range(n):
                    for j in range(i + 1, n):
                        if arr[i] & arr[j] == k:
                            arr[i], arr[j] = arr[j], arr[i]
                            changed = True

            if arr == sorted(nums):
                return k

        return 0
```

python
```
# Optimal — O(n)
class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        ans = -1

        for i, num in enumerate(nums):
            if i != num:
                ans &= num

        return max(ans, 0)
```
