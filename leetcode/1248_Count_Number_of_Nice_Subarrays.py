# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.



# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example 2:

# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
# Example 3:

# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16


# Constraints:

# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length
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
```
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            odd = 0

            for j in range(i, n):
                if nums[j] % 2:
                    odd += 1

                if odd == k:
                    ans += 1
                elif odd > k:
                    break

        return ans
```

### Optimal — Sliding Window

python
```
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def atMost(k):
            left = 0
            odd = 0
            count = 0

            for right in range(len(nums)):
                odd += nums[right] % 2

                while odd > k:
                    odd -= nums[left] % 2
                    left += 1

                count += right - left + 1

            return count

        return atMost(k) - atMost(k - 1)
```
