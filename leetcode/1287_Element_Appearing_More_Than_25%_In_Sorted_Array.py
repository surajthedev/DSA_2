# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.



# Example 1:

# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
# Example 2:

# Input: arr = [1,1]
# Output: 1


# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 105
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
### Brute Force

python

```

from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        count = Counter(arr)
        n = len(arr)

        for num in arr:
            if count[num] > n // 4:
                return num
```

### Optimal (Binary Search)

python

```

class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)

        for i in [n // 4, n // 2, 3 * n // 4]:
            num = arr[i]
            left = self.lower_bound(arr, num)
            right = self.upper_bound(arr, num)

            if right - left > n // 4:
                return num

    def lower_bound(self, arr, target):
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    def upper_bound(self, arr, target):
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2

            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return left
```
