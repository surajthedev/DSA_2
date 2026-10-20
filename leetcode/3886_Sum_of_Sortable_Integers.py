# You are given an integer array nums of length n.

# An integer k is called sortable if k divides n and you can sort nums in non-decreasing order by sequentially performing the following operations:

# Partition nums into consecutive subarrays of length k.
# Cyclically rotate each subarray independently any number of times to the left or to the right.
# Return an integer denoting the sum of all possible sortable integers k.



# Example 1:

# Input: nums = [3,1,2]

# Output: 3

# Explanation:​​​​​​​

# For n = 3, possible divisors are 1 and 3.
# For k = 1: each subarray has one element. No rotation can sort the array.
# For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.
# Only k = 3 is sortable. Hence, the answer is 3.
# Example 2:

# Input: nums = [7,6,5]

# Output: 0

# Explanation:

# For n = 3, possible divisors are 1 and 3.
# For k = 1: each subarray has one element. No rotation can sort the array.
# For k = 3: the single subarray [7, 6, 5] cannot be rotated into non-decreasing order.
# No k is sortable. Hence, the answer is 0.
# Example 3:

# Input: nums = [5,8]

# Output: 3

# Explanation:​​​​​​​

# For n = 2, possible divisors are 1 and 2.
# Since [5, 8] is already sorted, every divisor is sortable. Hence, the answer is 1 + 2 = 3.


# Constraints:

# 1 <= n == nums.length <= 105
# 1 <= nums[i] <= 105
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
# Brute Force:
from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            ok = True
            prev_last = None
            for i in range(0, n, k):
                block = nums[i:i + k]
                found = None
                for r in range(k):
                    rot = block[r:] + block[:r]
                    if all(rot[j] <= rot[j + 1] for j in range(k - 1)):
                        found = rot
                        break
                if found is None:
                    ok = False
                    break
                if prev_last is not None and prev_last > found[0]:
                    ok = False
                    break
                prev_last = found[-1]
            if ok:
                total += k
        return total













# Optimal:
from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            d = 1 if i + 1 < n and nums[i] > nums[i + 1] else 0
            pref[i + 1] = pref[i] + d

        total = 0
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            ok = True
            prev_max = 0
            for s in range(0, n, k):
                e = s + k - 1
                d = pref[e] - pref[s]
                if d == 0:
                    mn, mx = nums[s], nums[e]
                elif d == 1 and nums[e] <= nums[s]:
                    lo, hi = s, e - 1
                    while lo < hi:
                        mid = (lo + hi) // 2
                        if pref[mid + 1] - pref[s] >= 1:
                            hi = mid
                        else:
                            lo = mid + 1
                    mn, mx = nums[lo + 1], nums[lo]
                else:
                    ok = False
                    break
                if mn < prev_max:
                    ok = False
                    break
                prev_max = mx
            if ok:
                total += k
        return total
