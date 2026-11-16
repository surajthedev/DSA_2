# Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

# Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

# A subarray is defined as a contiguous block of elements in the array.



# Example 1:

# Input: nums = [3,1,4,2], p = 6
# Output: 1
# Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
# Example 2:

# Input: nums = [6,3,5,2], p = 9
# Output: 2
# Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
# Example 3:

# Input: nums = [1,2,3], p = 3
# Output: 0
# Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.


# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= p <= 109
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
# **Brute Force — O(n²)**

```
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p

        if target == 0:
            return 0

        n = len(nums)
        ans = n

        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]

                if curr % p == target:
                    ans = min(ans, j - i + 1)

        return ans if ans < n else -1```

**Optimal — O(n)**

```
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p

        if target == 0:
            return 0

        remainder = 0
        prefix = {0: -1}
        ans = len(nums)

        for i, num in enumerate(nums):
            remainder = (remainder + num) % p

            needed = (remainder - target) % p

            if needed in prefix:
                ans = min(ans, i - prefix[needed])

            prefix[remainder] = i

        return ans if ans < len(nums) else -1```
