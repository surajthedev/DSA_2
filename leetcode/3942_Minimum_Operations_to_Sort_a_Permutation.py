# You are given an integer array nums of length n, where nums is a permutation of the integers from 0 to n - 1.

# You may perform only the following operations:

# Reverse the entire array.
# Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.
# Return an integer denoting the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1.



# Example 1:

# Input: nums = [0,2,1]

# Output: 2

# Explanation:

# Rotate Left by one: [2, 1, 0]
# Reverse the array: [0, 1, 2]
# The array becomes sorted in 2 operations, which is minimal

# Example 2:

# Input: nums = [1,0,2]

# Output: 2

# Explanation:

# Reverse the array: [2, 0, 1]
# Rotate Left by one: [0, 1, 2]
# The array becomes sorted in 2 operations, which is minimal.

# Example 3:

# Input: nums = [2,0,1,3]

# Output: -1

# Explanation:

# It is impossible to reach [2, 0, 1, 3]. Thus, the answer is -1.



# Constraints:

# 1 <= n == nums.length <= 105
# 0 <= nums[i] <= n - 1
# nums is a permutation of integers from 0 to n - 1.
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
# ### Brute Force

from collections import deque
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        target = tuple(range(n))
        start = tuple(nums)

        if start == target:
            return 0

        visited = {start}
        q = deque([(start, 0)])

        while q:
            state, d = q.popleft()

            rev = state[::-1]
            rot = state[1:] + state[:1]

            for nxt in (rev, rot):
                if nxt == target:
                    return d + 1
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, d + 1))

        return -1
### Optimal

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        INF = float('inf')
        ans = INF

        # Case 1: cyclic ascending
        k = nums[0]
        if all(nums[i] == (k + i) % n for i in range(n)):
            if k == 0:
                ans = 0
            else:
                ans = min(ans, n - k, k + 2)

        # Case 2: cyclic descending
        if all(nums[i] == (k - i) % n for i in range(n)):
            # reverse first, then rotate left
            ans = min(ans, 1 + (n - k - 1) % n)
            # rotate left first, then reverse
            ans = min(ans, (k + 1) % n + 1)

        return -1 if ans == INF else ans
