# You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

# 0 <= i < j < nums.length
# nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
# Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.



# Example 1:

# Input: nums = [42,11,1,97]
# Output: 2
# Explanation: The two pairs are:
#  - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
#  - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
# Example 2:

# Input: nums = [13,10,35,24,76]
# Output: 4


# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
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

python

```python

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        ans = 0

        def rev(x):
            return int(str(x)[::-1])

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]):
                    ans += 1

        return ans % MOD
```

Time Complexity: O(n² × d) Space Complexity: O(d)

### Optimal (HashMap + Math)

Optimalpython

```python

from collections import defaultdict
from typing import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        freq = defaultdict(int)
        ans = 0

        for num in nums:
            rev = int(str(num)[::-1])
            diff = num - rev

            ans = (ans + freq[diff]) % MOD
            freq[diff] += 1

        return ans
```

Time Complexity: O(n × d) Space Complexity: O(n)

`d` = number of digits in the largest number.
