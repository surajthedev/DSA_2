# You are given an array of integers nums (0-indexed) and an integer k.

# The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

# Return the maximum possible score of a good subarray.



# Example 1:

# Input: nums = [1,4,3,7,4,5], k = 3
# Output: 15
# Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15.
# Example 2:

# Input: nums = [5,5,4,5,4,1,1,1], k = 0
# Output: 20
# Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.


# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 2 * 104
# 0 <= k < nums.length
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
# ### 1. Brute Force — O(n²)

python

```python
class Solution:
    def maximumScore(self, nums, k):
        n = len(nums)
        ans = 0

        for i in range(k + 1):
            mn = float('inf')

            for j in range(i, n):
                mn = min(mn, nums[j])

                if j >= k:
                    ans = max(ans, mn * (j - i + 1))

        return ans
```

### 2. Optimal — O(n)

python

```python
class Solution:
    def maximumScore(self, nums, k):
        left = right = k
        mn = nums[k]
        ans = mn

        n = len(nums)

        while left > 0 or right < n - 1:
            if left == 0:
                right += 1
                mn = min(mn, nums[right])

            elif right == n - 1:
                left -= 1
                mn = min(mn, nums[left])

            elif nums[left - 1] > nums[right + 1]:
                left -= 1
                mn = min(mn, nums[left])

            else:
                right += 1
                mn = min(mn, nums[right])

            ans = max(ans, mn * (right - left + 1))

        return ans
```
