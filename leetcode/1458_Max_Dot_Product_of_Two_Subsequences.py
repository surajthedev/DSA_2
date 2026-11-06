# Given two arrays nums1 and nums2.

# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

# A subsequence of an array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).



# Example 1:

# Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# Output: 18
# Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
# Their dot product is (2*3 + (-2)*(-6)) = 18.
# Example 2:

# Input: nums1 = [3,-2], nums2 = [2,-6,7]
# Output: 21
# Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
# Their dot product is (3*7) = 21.
# Example 3:

# Input: nums1 = [-1,-1], nums2 = [1,1]
# Output: -1
# Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
# Their dot product is -1.


# Constraints:

# 1 <= nums1.length, nums2.length <= 500
# -1000 <= nums1[i], nums2[i] <= 1000
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
# ### 1. Brute Force — Python (Recursion + Memoization)

python

```python
from functools import lru_cache

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        @lru_cache(None)
        def dfs(i, j):
            if i == len(nums1) or j == len(nums2):
                return float('-inf')

            product = nums1[i] * nums2[j]

            take = product + max(0, dfs(i + 1, j + 1))

            skip1 = dfs(i + 1, j)
            skip2 = dfs(i, j + 1)

            return max(take, skip1, skip2)

        return dfs(0, 0)
```

Time Complexity: $O(N \times M)$

Space Complexity: $O(N \times M)$

### 2. Optimal — Python (Dynamic Programming)

python

```python
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)

        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                product = nums1[i] * nums2[j]

                take = product + max(0, dp[i + 1][j + 1])

                skip1 = dp[i + 1][j]
                skip2 = dp[i][j + 1]

                dp[i][j] = max(take, skip1, skip2)

        return dp[0][0]
```

Time Complexity: $O(N \times M)$

Space Complexity: $O(N \times M)$
