# You are given an integer array, nums, and an integer k. nums comprises of only 0's and 1's. In one move, you can choose two adjacent indices and swap their values.

# Return the minimum number of moves required so that nums has k consecutive 1's.



# Example 1:

# Input: nums = [1,0,0,1,0,1], k = 2
# Output: 1
# Explanation: In 1 move, nums could be [1,0,0,0,1,1] and have 2 consecutive 1's.
# Example 2:

# Input: nums = [1,0,0,0,0,0,1,1], k = 3
# Output: 5
# Explanation: In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0,1,1,1].
# Example 3:

# Input: nums = [1,1,0,1], k = 2
# Output: 0
# Explanation: nums already has 2 consecutive 1's.


# Constraints:

# 1 <= nums.length <= 105
# nums[i] is 0 or 1.
# 1 <= k <= sum(nums)
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
    def minMoves(self, nums: List[int], k: int) -> int:
        positions = [i for i, num in enumerate(nums) if num == 1]

        ans = float('inf')

        for i in range(len(positions) - k + 1):
            group = positions[i:i+k]

            moves = 0
            median = group[k // 2]

            for j in range(k):
                moves += abs(group[j] - (median - k // 2 + j))

            ans = min(ans, moves)

        return ans
```

Time Complexity: O(n × k)

Space Complexity: O(n)

### 2. Optimal Approach (Sliding Window + Prefix Sum)

Optimalpython

```python

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        positions = [i for i, num in enumerate(nums) if num == 1]

        for i in range(len(positions)):
            positions[i] -= i

        prefix = [0]

        for x in positions:
            prefix.append(prefix[-1] + x)

        ans = float('inf')
        m = len(positions)

        for i in range(m - k + 1):
            mid = i + k // 2

            left = positions[mid] * (mid - i) - (prefix[mid] - prefix[i])

            right = (prefix[i + k] - prefix[mid + 1]) - positions[mid] * (i + k - mid - 1)

            ans = min(ans, left + right)

        return ans
```

Time Complexity: O(n)

Space Complexity: O(n)
