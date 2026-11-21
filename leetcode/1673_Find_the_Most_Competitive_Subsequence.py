# Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

# An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

# We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.



# Example 1:

# Input: nums = [3,5,2,6], k = 2
# Output: [2,6]
# Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
# Example 2:

# Input: nums = [2,4,3,3,5,4,9,6], k = 4
# Output: [2,3,3,4]


# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
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
#
#
#
#
#
#
#
# ### 1. Brute Force Approach

Time: O(N × K) | Space: O(K)

python

```python
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        ans = []
        start = 0
        n = len(nums)

        for i in range(k):
            end = n - (k - i) + 1
            min_idx = start

            for j in range(start, end):
                if nums[j] < nums[min_idx]:
                    min_idx = j

            ans.append(nums[min_idx])
            start = min_idx + 1

        return ans
```

### 2. Optimal Approach (Monotonic Stack)

Time: O(N) — Space: O(N)python

```python
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)

        for i, num in enumerate(nums):
            while stack and stack[-1] > num and len(stack) + n - i > k:
                stack.pop()

            if len(stack) < k:
                stack.append(num)

        return stack
```
