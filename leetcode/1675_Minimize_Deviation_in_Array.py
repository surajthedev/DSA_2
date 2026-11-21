# You are given an array nums of n positive integers.

# You can perform two types of operations on any element of the array any number of times:

# If the element is even, divide it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
# If the element is odd, multiply it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
# The deviation of the array is the maximum difference between any two elements in the array.

# Return the minimum deviation the array can have after performing some number of operations.



# Example 1:

# Input: nums = [1,2,3,4]
# Output: 1
# Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
# Example 2:

# Input: nums = [4,1,5,20,3]
# Output: 3
# Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
# Example 3:

# Input: nums = [2,10,8]
# Output: 3


# Constraints:

# n == nums.length
# 2 <= n <= 5 * 104
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
#
#
#
# ### 1. Brute Force Approach

Time: O(N × log² M) — Space: O(N)python

```python
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        values = []

        for num in nums:
            if num % 2 == 1:
                num *= 2
            values.append(num)

        ans = float('inf')

        while True:
            minimum = min(values)
            maximum = max(values)

            ans = min(ans, maximum - minimum)

            if maximum % 2 == 1:
                break

            idx = values.index(maximum)
            values[idx] //= 2

        return ans
```

### 2. Optimal Approach (Max Heap + Greedy)

Time: O(N log M log N) — Space: O(N)python

```python
import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        min_val = float('inf')
        max_heap = []

        for num in nums:
            if num % 2 == 1:
                num *= 2

            min_val = min(min_val, num)
            heapq.heappush(max_heap, -num)

        ans = float('inf')

        while True:
            maximum = -heapq.heappop(max_heap)

            ans = min(ans, maximum - min_val)

            if maximum % 2 == 1:
                break

            maximum //= 2

            min_val = min(min_val, maximum)

            heapq.heappush(max_heap, -maximum)

        return ans
```
