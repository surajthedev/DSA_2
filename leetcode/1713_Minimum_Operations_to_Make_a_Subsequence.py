# You are given an array target that consists of distinct integers and another integer array arr that can have duplicates.

# In one operation, you can insert any integer at any position in arr. For example, if arr = [1,4,1,2], you can add 3 in the middle and make it [1,4,3,1,2]. Note that you can insert the integer at the very beginning or end of the array.

# Return the minimum number of operations needed to make target a subsequence of arr.

# A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.



# Example 1:

# Input: target = [5,1,3], arr = [9,4,2,3,4]
# Output: 2
# Explanation: You can add 5 and 1 in such a way that makes arr = [5,9,4,1,2,3,4], then target will be a subsequence of arr.
# Example 2:

# Input: target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]
# Output: 3


# Constraints:

# 1 <= target.length, arr.length <= 105
# 1 <= target[i], arr[i] <= 109
# target contains no duplicates.
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
#
#
# ### 1. Brute Force Approach (LCS)

python

```python
from typing import List

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        n = len(target)
        m = len(arr)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if target[i - 1] == arr[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return n - dp[n][m]
```

Time Complexity: $O(n \times m)$

Space Complexity: $O(n \times m)$

### 2. Optimal Approach (HashMap + LIS + Binary Search)

python

```python
from typing import List
from bisect import bisect_left

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        pos = {num: i for i, num in enumerate(target)}

        lis = []

        for num in arr:
            if num in pos:
                idx = pos[num]

                k = bisect_left(lis, idx)

                if k == len(lis):
                    lis.append(idx)
                else:
                    lis[k] = idx

        return len(target) - len(lis)
```

Time Complexity: $O(n + m\log n)$

Space Complexity: $O(n)$
