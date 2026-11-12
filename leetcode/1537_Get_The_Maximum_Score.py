# You are given two sorted arrays of distinct integers nums1 and nums2.

# A valid path is defined as follows:

# Choose array nums1 or nums2 to traverse (from index-0).
# Traverse the current array from left to right.
# If you are reading any value that is present in nums1 and nums2 you are allowed to change your path to the other array. (Only one repeated value is considered in the valid path).
# The score is defined as the sum of unique values in a valid path.

# Return the maximum score you can obtain of all possible valid paths. Since the answer may be too large, return it modulo 109 + 7.



# Example 1:


# Input: nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
# Output: 30
# Explanation: Valid paths:
# [2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],  (starting from nums1)
# [4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]    (starting from nums2)
# The maximum is obtained with the path in green [2,4,6,8,10].
# Example 2:

# Input: nums1 = [1,3,5,7,9], nums2 = [3,5,100]
# Output: 109
# Explanation: Maximum sum is obtained with the path [1,3,5,100].
# Example 3:

# Input: nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]
# Output: 40
# Explanation: There are no common elements between nums1 and nums2.
# Maximum sum is obtained with the path [6,7,8,9,10].


# Constraints:

# 1 <= nums1.length, nums2.length <= 105
# 1 <= nums1[i], nums2[i] <= 107
# nums1 and nums2 are strictly increasing.
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
# ### 1. Brute Force – O(n × m)

python

```python
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7

        def calculate(arr1, arr2):
            total = 0
            i = j = 0
            sum1 = sum2 = 0

            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    sum1 += arr1[i]
                    i += 1

                elif arr1[i] > arr2[j]:
                    sum2 += arr2[j]
                    j += 1

                else:
                    total += max(sum1, sum2) + arr1[i]
                    sum1 = sum2 = 0
                    i += 1
                    j += 1

            sum1 += sum(arr1[i:])
            sum2 += sum(arr2[j:])

            return (total + max(sum1, sum2)) % MOD

        return calculate(nums1, nums2)
```

### 2. Optimal – Two Pointers | O(n + m)

python

```python
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7

        i = j = 0
        sum1 = sum2 = 0

        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1

            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1

            else:
                best = max(sum1, sum2) + nums1[i]

                sum1 = best
                sum2 = best

                i += 1
                j += 1

        sum1 += sum(nums1[i:])
        sum2 += sum(nums2[j:])

        return max(sum1, sum2) % MOD
```
