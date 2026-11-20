# You are given an array of n integers, nums, where there are at most 50 unique values in the array. You are also given an array of m customer order quantities, quantity, where quantity[i] is the amount of integers the ith customer ordered. Determine if it is possible to distribute nums such that:

# The ith customer gets exactly quantity[i] integers,
# The integers the ith customer gets are all equal, and
# Every customer is satisfied.
# Return true if it is possible to distribute nums according to the above conditions.



# Example 1:

# Input: nums = [1,2,3,4], quantity = [2]
# Output: false
# Explanation: The 0th customer cannot be given two different integers.
# Example 2:

# Input: nums = [1,2,3,3], quantity = [2]
# Output: true
# Explanation: The 0th customer is given [3,3]. The integers [1,2] are not used.
# Example 3:

# Input: nums = [1,1,2,2], quantity = [2,2]
# Output: true
# Explanation: The 0th customer is given [1,1], and the 1st customer is given [2,2].


# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= 1000
# m == quantity.length
# 1 <= m <= 10
# 1 <= quantity[i] <= 105
# There are at most 50 unique values in nums.
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
# ### Brute Force — Backtracking

python

```python
from collections import Counter
from typing import List

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        freq = list(Counter(nums).values())
        quantity.sort(reverse=True)

        def backtrack(i):
            if i == len(quantity):
                return True

            for j in range(len(freq)):
                if freq[j] >= quantity[i]:
                    freq[j] -= quantity[i]

                    if backtrack(i + 1):
                        return True

                    freq[j] += quantity[i]

            return False

        return backtrack(0)
```

### Optimal Approach — Bitmask DP

python

```python
from collections import Counter
from typing import List

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        freq = sorted(Counter(nums).values(), reverse=True)
        quantity.sort(reverse=True)

        m = len(quantity)
        total = 1 << m

        subset_sum = [0] * total

        for mask in range(1, total):
            bit = mask & -mask
            i = bit.bit_length() - 1
            subset_sum[mask] = subset_sum[mask ^ bit] + quantity[i]

        dp = [False] * total
        dp[0] = True

        for count in freq:
            new_dp = dp[:]

            for mask in range(total):
                if not dp[mask]:
                    continue

                remaining = (total - 1) ^ mask
                sub = remaining

                while sub:
                    if subset_sum[sub] <= count:
                        new_dp[mask | sub] = True

                    sub = (sub - 1) & remaining

            dp = new_dp

            if dp[-1]:
                return True

        return dp[-1]
```
