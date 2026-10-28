# You are given an integer array nums. The value of this array is defined as the sum of |nums[i] - nums[i + 1]| for all 0 <= i < nums.length - 1.

# You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.

# Find maximum possible value of the final array.



# Example 1:

# Input: nums = [2,3,1,5,4]
# Output: 10
# Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4] whose value is 10.
# Example 2:

# Input: nums = [2,4,9,24,2,1,10]
# Output: 68


# Constraints:

# 2 <= nums.length <= 3 * 104
# -105 <= nums[i] <= 105
# The answer is guaranteed to fit in a 32-bit integer.
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
# ### 1. Brute Force

python

```
class Solution:
    def maxValueAfterReverse(self, nums: list[int]) -> int:
        n = len(nums)

        def calculate(arr):
            return sum(abs(arr[i] - arr[i + 1]) for i in range(len(arr) - 1))

        ans = calculate(nums)

        for i in range(n):
            for j in range(i + 1, n):
                arr = nums[:]
                arr[i:j + 1] = reversed(arr[i:j + 1])
                ans = max(ans, calculate(arr))

        return ans
```

Time Complexity: $O(n^3)$

### 2. Optimal — Greedy

python

```
class Solution:
    def maxValueAfterReverse(self, nums: list[int]) -> int:
        n = len(nums)
        total = sum(abs(nums[i] - nums[i + 1]) for i in range(n - 1))

        gain = 0

        for i in range(1, n - 1):
            gain = max(
                gain,
                abs(nums[0] - nums[i + 1]) - abs(nums[i] - nums[i + 1]),
                abs(nums[n - 1] - nums[i - 1]) - abs(nums[i] - nums[i - 1])
            )

        high = float('-inf')
        low = float('inf')

        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            high = max(high, min(a, b))
            low = min(low, max(a, b))

        gain = max(gain, 2 * (high - low))

        return total + gain
```

Time Complexity: $O(n)$

Space Complexity: $O(1)$
