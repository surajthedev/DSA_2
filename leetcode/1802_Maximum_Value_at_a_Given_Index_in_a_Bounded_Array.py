# You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

# nums.length == n
# nums[i] is a positive integer where 0 <= i < n.
# abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
# The sum of all the elements of nums does not exceed maxSum.
# nums[index] is maximized.
# Return nums[index] of the constructed array.

# Note that abs(x) equals x if x >= 0, and -x otherwise.



# Example 1:

# Input: n = 4, index = 2,  maxSum = 6
# Output: 2
# Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
# There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
# Example 2:

# Input: n = 6, index = 1,  maxSum = 10
# Output: 3


# Constraints:

# 1 <= n <= maxSum <= 109
# 0 <= index < n
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
# ### Brute Force (Binary Search + Sum Calculation)

python

```python

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def calculate(peak, length):
            if peak > length:
                return (peak + peak - length + 1) * length // 2
            return (peak + 1) * peak // 2 + (length - peak)

        def isPossible(mid):
            left = calculate(mid - 1, index)
            right = calculate(mid - 1, n - index - 1)

            total = left + right + mid

            return total <= maxSum

        low, high = 1, maxSum

        while low <= high:
            mid = (low + high) // 2

            if isPossible(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high
```

Time Complexity: O(log maxSum) Space Complexity: O(1)

### Optimal (Binary Search + Math)

Optimalpython

```python

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def sideSum(peak, length):
            if peak > length:
                return (peak + peak - length + 1) * length // 2
            return peak * (peak - 1) // 2 + length

        def isPossible(mid):
            total = mid

            total += sideSum(mid - 1, index)
            total += sideSum(mid - 1, n - index - 1)

            return total <= maxSum

        low, high = 1, maxSum

        while low <= high:
            mid = (low + high) // 2

            if isPossible(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high
```

Time Complexity: O(log maxSum) Space Complexity: O(1)
