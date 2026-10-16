# You are given a 0-indexed integer array nums.

# The distinct count of a subarray of nums is defined as:

# Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
# Return the sum of the squares of distinct counts of all subarrays of nums.

# Since the answer may be very large, return it modulo 109 + 7.

# A subarray is a contiguous non-empty sequence of elements within an array.



# Example 1:

# Input: nums = [1,2,1]
# Output: 15
# Explanation: Six possible subarrays are:
# [1]: 1 distinct value
# [2]: 1 distinct value
# [1]: 1 distinct value
# [1,2]: 2 distinct values
# [2,1]: 2 distinct values
# [1,2,1]: 2 distinct values
# The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.
# Example 2:

# Input: nums = [2,2]
# Output: 3
# Explanation: Three possible subarrays are:
# [2]: 1 distinct value
# [2]: 1 distinct value
# [2,2]: 1 distinct value
# The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.


# Constraints:

# 1 <= nums.length <= 105
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
#
#
#
#
# Solution:
class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        s1 = [0] * (4 * n)   # sum of d[i]
        s2 = [0] * (4 * n)   # sum of d[i]^2
        lz = [0] * (4 * n)   # lazy add

        def apply(node, length, v):
            # d -> d+v for every element in this node's range
            s2[node] += 2 * v * s1[node] + length * v * v
            s1[node] += length * v
            lz[node] += v

        def push(node, l, r):
            if lz[node]:
                m = (l + r) // 2
                apply(2 * node, m - l + 1, lz[node])
                apply(2 * node + 1, r - m, lz[node])
                lz[node] = 0

        def update(node, l, r, ql, qr):
            if qr < l or r < ql:
                return
            if ql <= l and r <= qr:
                apply(node, r - l + 1, 1)
                return
            push(node, l, r)
            m = (l + r) // 2
            update(2 * node, l, m, ql, qr)
            update(2 * node + 1, m + 1, r, ql, qr)
            s1[node] = s1[2 * node] + s1[2 * node + 1]
            s2[node] = s2[2 * node] + s2[2 * node + 1]

        last = {}
        ans = 0
        for j, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, j)
            last[x] = j
            ans = (ans + s2[1]) % MOD

        return ans
