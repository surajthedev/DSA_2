# Given an array of integers arr, return the number of subarrays with an odd sum.

# Since the answer can be very large, return it modulo 109 + 7.



# Example 1:

# Input: arr = [1,3,5]
# Output: 4
# Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
# All sub-arrays sum are [1,4,9,3,8,5].
# Odd sums are [1,9,3,5] so the answer is 4.
# Example 2:

# Input: arr = [2,4,6]
# Output: 0
# Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
# All sub-arrays sum are [2,6,12,4,10,6].
# All sub-arrays have even sum and the answer is 0.
# Example 3:

# Input: arr = [1,2,3,4,5,6,7]
# Output: 16


# Constraints:

# 1 <= arr.length <= 105
# 1 <= arr[i] <= 100
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
# ### Brute Force — O(n²)

python

```python
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        count = 0

        for i in range(len(arr)):
            total = 0

            for j in range(i, len(arr)):
                total += arr[j]

                if total % 2 == 1:
                    count += 1

        return count % MOD
```

### Optimal Solution — O(n)

python

```python
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        odd = 0
        even = 1
        prefix = 0
        ans = 0

        for num in arr:
            prefix += num

            if prefix % 2 == 0:
                ans += odd
                even += 1
            else:
                ans += even
                odd += 1

        return ans % MOD
```
