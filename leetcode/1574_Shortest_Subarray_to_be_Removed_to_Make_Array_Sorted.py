# Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

# Return the length of the shortest subarray to remove.

# A subarray is a contiguous subsequence of the array.



# Example 1:

# Input: arr = [1,2,3,10,4,2,3,5]
# Output: 3
# Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
# Another correct solution is to remove the subarray [3,10,4].
# Example 2:

# Input: arr = [5,4,3,2,1]
# Output: 4
# Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
# Example 3:

# Input: arr = [1,2,3]
# Output: 0
# Explanation: The array is already non-decreasing. We do not need to remove any elements.


# Constraints:

# 1 <= arr.length <= 105
# 0 <= arr[i] <= 109
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
# ### 1. Brute Force Approach

python

```python
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        ans = n

        for i in range(n + 1):
            for j in range(i, n + 1):
                remaining = arr[:i] + arr[j:]

                if all(remaining[k] <= remaining[k + 1]
                       for k in range(len(remaining) - 1)):
                    ans = min(ans, j - i)

        return ans
```

Time Complexity: O(n³) Space Complexity: O(n)

### 2. Optimal Approach (Two Pointers + Greedy)

python

```python
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        if left == n - 1:
            return 0

        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        ans = min(n - left - 1, right)

        i, j = 0, right

        while i <= left and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1

        return ans
```

Time Complexity: O(n) Space Complexity: O(1)
