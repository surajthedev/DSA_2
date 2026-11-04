# Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.



# Example 1:


# Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,2,7,5,3,8,6,9]
# Example 2:


# Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]


# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i].length <= 105
# 1 <= sum(nums[i].length) <= 105
# 1 <= nums[i][j] <= 105
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
# ### 1. Brute Force Approach (Diagonal Grouping)

python

```python
from collections import defaultdict
from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i + j].append(nums[i][j])

        result = []

        for key in sorted(diagonals):
            result.extend(diagonals[key][::-1])

        return result
```

Time Complexity: $O(N + D\log D)$

Space Complexity: $O(N)$

### 2. Optimal Approach (BFS)

python

```python
from collections import deque
from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        result = []
        queue = deque([(0, 0)])

        while queue:
            i, j = queue.popleft()
            result.append(nums[i][j])

            if j == 0 and i + 1 < len(nums):
                queue.append((i + 1, j))

            if j + 1 < len(nums[i]):
                queue.append((i, j + 1))

        return result
```

Time Complexity: $O(N)$

Space Complexity: $O(N)$
