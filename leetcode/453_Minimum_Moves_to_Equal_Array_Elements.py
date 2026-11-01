# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

# In one move, you can increment n - 1 elements of the array by 1.



# Example 1:

# Input: nums = [1,2,3]
# Output: 3
# Explanation: Only three moves are needed (remember each move increments two elements):
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# Example 2:

# Input: nums = [1,1,1]
# Output: 0


# Constraints:

# n == nums.length
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# The answer is guaranteed to fit in a 32-bit integer.
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
### Brute Force

python

```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves = 0

        while len(set(nums)) > 1:
            max_num = max(nums)

            for i in range(len(nums)):
                if nums[i] != max_num:
                    nums[i] += 1

            moves += 1

        return moves
```

### Optimal Approach

python

```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        moves = 0

        for num in nums:
            moves += num - min_num

        return moves
```
