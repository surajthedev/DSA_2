# You are given an integer array nums.

# Find the minimum length of a subarray that is not identical to any other subarray in nums.

# Return an integer denoting the minimum possible length of such a subarray.

# Two subarrays are considered identical if they have the same length and the same elements in corresponding positions.



# Example 1:

# Input: nums = [3,3,3]

# Output: 3

# Explanation:

# Subarrays of length 1: [3] → appears 3 times
# Subarrays of length 2: [3, 3] → appears 2 times
# Subarrays of length 3: [3, 3, 3] → appears once
# The subarray [3, 3, 3] is unique, so the smallest unique subarray length is 3.

# Example 2:

# Input: nums = [2,1,2,3,3]

# Output: 1

# Explanation:

# Subarrays of length 1:

# [2] → appears 2 times
# [1] → appears once
# [3] → appears 2 times
# The subarray [1] is unique, so the smallest unique subarray length is 1.
# Example 3:

# Input: nums = [1,1,2,2,1]

# Output: 2

# Explanation:

# Subarrays of length 1:

# [1] → appears 3 times
# [2] → appears 2 times
# Subarrays of length 2:

# [1, 1] → appears once
# [1, 2] → appears once
# [2, 2] → appears once
# [2, 1] → appears once
# There is at least one subarray of length 2 that is unique, so the smallest unique subarray length is 2.


# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
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
#
# ### Brute Force — Python

python

```python

class Solution:
    def minLength(self, nums: List[int]) -> int:
        n = len(nums)

        for k in range(1, n + 1):
            freq = {}

            for i in range(n - k + 1):
                sub = tuple(nums[i:i + k])
                freq[sub] = freq.get(sub, 0) + 1

            for count in freq.values():
                if count == 1:
                    return k

        return n
```

### Optimal — Python (Hashing + Binary Search)

python

```python

class Solution:
    def minLength(self, nums: List[int]) -> int:
        n = len(nums)

        def has_unique(k):
            seen = set()

            for i in range(n - k + 1):
                sub = tuple(nums[i:i + k])

                if sub in seen:
                    continue

                seen.add(sub)

            return len(seen) == n - k + 1

        left, right = 1, n
        ans = n

        while left <= right:
            mid = (left + right) // 2

            if has_unique(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
```
