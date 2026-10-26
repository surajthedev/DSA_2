# Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

# Return true if it is possible. Otherwise, return false.



# Example 1:

# Input: nums = [1,2,3,3,4,4,5,6], k = 4
# Output: true
# Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
# Example 2:

# Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# Output: true
# Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
# Example 3:

# Input: nums = [1,2,3,4], k = 3
# Output: false
# Explanation: Each array should be divided in subarrays of size 3.


# Constraints:

# 1 <= k <= nums.length <= 105
# 1 <= nums[i] <= 109
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

```

from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        nums.sort()
        count = Counter(nums)

        for num in nums:
            if count[num] == 0:
                continue

            for x in range(num, num + k):
                if count[x] == 0:
                    return False
                count[x] -= 1

        return True
```

### Optimal (Greedy + Min Heap)

python

```

from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        count = Counter(nums)

        for num in sorted(count):
            if count[num] > 0:
                freq = count[num]

                for x in range(num, num + k):
                    if count[x] < freq:
                        return False
                    count[x] -= freq

        return True
```
