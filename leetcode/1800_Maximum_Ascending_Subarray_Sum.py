# Given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray in nums.

# A subarray is defined as a contiguous sequence of numbers in an array.



# Example 1:

# Input: nums = [10,20,30,5,10,50]
# Output: 65
# Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
# Example 2:

# Input: nums = [10,20,30,40,50]
# Output: 150
# Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
# Example 3:

# Input: nums = [12,17,15,13,10,11,12]
# Output: 33
# Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.


# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
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

```python

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            curr_sum = nums[i]

            for j in range(i + 1, n):
                if nums[j] > nums[j - 1]:
                    curr_sum += nums[j]
                else:
                    break

            ans = max(ans, curr_sum)

        return ans
```

Time Complexity: O(n²) Space Complexity: O(1)

### Optimal (Greedy)

Optimalpython

```python

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        ans = curr_sum

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]

            ans = max(ans, curr_sum)

        return ans
```

Time Complexity: O(n) Space Complexity: O(1)
