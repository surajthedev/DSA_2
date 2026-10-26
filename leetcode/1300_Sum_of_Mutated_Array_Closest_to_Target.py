# Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

# In case of a tie, return the minimum such integer.

# Notice that the answer is not neccesarilly a number from arr.



# Example 1:

# Input: arr = [4,9,3], target = 10
# Output: 3
# Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
# Example 2:

# Input: arr = [2,3,5], target = 10
# Output: 5
# Example 3:

# Input: arr = [60864,25176,27249,21296,20204], target = 56803
# Output: 11361


# Constraints:

# 1 <= arr.length <= 104
# 1 <= arr[i], target <= 105
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

```

class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        best_value = 0
        min_diff = float('inf')

        for value in range(1, max(arr) + 1):
            total = sum(min(num, value) for num in arr)
            diff = abs(total - target)

            if diff < min_diff:
                min_diff = diff
                best_value = value

        return best_value
```

### Optimal (Binary Search)

python

```

class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        left, right = 0, max(arr)

        while left < right:
            mid = (left + right) // 2
            total = sum(min(num, mid) for num in arr)

            if total < target:
                left = mid + 1
            else:
                right = mid

        def get_sum(value):
            return sum(min(num, value) for num in arr)

        if left > 0 and abs(get_sum(left - 1) - target) <= abs(get_sum(left) - target):
            return left - 1

        return left
```
