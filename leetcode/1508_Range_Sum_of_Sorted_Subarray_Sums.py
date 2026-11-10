# You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

# Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.



# Example 1:

# Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
# Output: 13
# Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13.
# Example 2:

# Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
# Output: 6
# Explanation: The given array is the same as example 1. We have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to ri = 4 is 3 + 3 = 6.
# Example 3:

# Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
# Output: 50


# Constraints:

# n == nums.length
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 100
# 1 <= left <= right <= n * (n + 1) / 2
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
#Sorry, previous optimal solution mein sliding window ka calculation incorrect tha. Ye corrected code hai.

### 1. Brute Force

python

```python
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []

        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                arr.append(total)

        arr.sort()

        return sum(arr[left - 1:right]) % (10**9 + 7)
```

### 2. Optimal Solution (Binary Search + Sliding Window)

python

```python
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7

        def count_and_sum(target):
            count = 0
            total = 0
            window_sum = 0
            window_total = 0
            start = 0

            for end in range(n):
                window_sum += nums[end]
                window_total += nums[end] * (end - start + 1)

                while window_sum > target:
                    window_total -= window_sum
                    window_sum -= nums[start]
                    start += 1

                count += end - start + 1
                total += window_total

            return count, total

        def sum_k(k):
            if k == 0:
                return 0

            low = min(nums)
            high = sum(nums)

            while low < high:
                mid = (low + high) // 2
                count, _ = count_and_sum(mid)

                if count >= k:
                    high = mid
                else:
                    low = mid + 1

            count, total = count_and_sum(low)

            return total - (count - k) * low

        return (sum_k(right) - sum_k(left - 1)) % MOD
```

Expected outputs:

- `[1,2,3,4], left=1, right=5` → `13`
- `[1,2,3,4], left=3, right=4` → `6`
- `[1,2,3,4], left=1, right=10` → `50`
