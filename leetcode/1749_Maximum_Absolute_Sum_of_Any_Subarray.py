# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

# Return the maximum absolute sum of any (possibly empty) subarray of nums.

# Note that abs(x) is defined as follows:

# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.


# Example 1:

# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
# Example 2:

# Input: nums = [2,-5,1,-4,3,-2]
# Output: 8
# Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.


# Constraints:

# 1 <= nums.length <= 105
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
#
#
#
#
# ### Brute Force

python

```python
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                ans = max(ans, abs(total))

        return ans
```

### Optimal (Kadane's Algorithm)

python

```python
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0
        curr_max = 0
        curr_min = 0

        for num in nums:
            curr_max = max(0, curr_max + num)
            curr_min = min(0, curr_min + num)

            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)

        return max(max_sum, abs(min_sum))
```
