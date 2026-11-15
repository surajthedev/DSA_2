# Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the following rules:

# Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
# Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.


# Example 1:

# Input: nums1 = [7,4], nums2 = [5,2,8,9]
# Output: 1
# Explanation: Type 1: (1, 1, 2), nums1[1]2 = nums2[1] * nums2[2]. (42 = 2 * 8).
# Example 2:

# Input: nums1 = [1,1], nums2 = [1,1,1]
# Output: 9
# Explanation: All Triplets are valid, because 12 = 1 * 1.
# Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]2 = nums2[j] * nums2[k].
# Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]2 = nums1[j] * nums1[k].
# Example 3:

# Input: nums1 = [7,7,8,3], nums2 = [1,2,9,7]
# Output: 2
# Explanation: There are 2 valid triplets.
# Type 1: (3,0,2).  nums1[3]2 = nums2[0] * nums2[2].
# Type 2: (3,0,1).  nums2[3]2 = nums1[0] * nums1[1].


# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 1 <= nums1[i], nums2[i] <= 105
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
# ### **1. Brute Force — O(n × m² + m × n²)**

```
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0

        for num in nums1:
            target = num * num

            for j in range(len(nums2)):
                for k in range(j + 1, len(nums2)):
                    if nums2[j] * nums2[k] == target:
                        count += 1

        for num in nums2:
            target = num * num

            for j in range(len(nums1)):
                for k in range(j + 1, len(nums1)):
                    if nums1[j] * nums1[k] == target:
                        count += 1

        return count```

### **2. Optimal — O(n² + m²)**

```
from collections import Counter

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def countTriplets(arr1, arr2):
            freq = Counter(arr2)
            count = 0

            for num in arr1:
                target = num * num

                for x in freq:
                    if target % x == 0:
                        y = target // x

                        if y in freq:
                            if x == y:
                                count += freq[x] * (freq[x] - 1) // 2
                            elif x < y:
                                count += freq[x] * freq[y]

            return count

        return countTriplets(nums1, nums2) + countTriplets(nums2, nums1)```
