# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

# Return the largest lucky integer in the array. If there is no lucky integer return -1.



# Example 1:

# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:

# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
# Example 3:

# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.


# Constraints:

# 1 <= arr.length <= 500
# 1 <= arr[i] <= 500
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
# ## 1. Brute Force Approach

python

```python
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = -1

        for num in arr:
            count = 0

            for x in arr:
                if x == num:
                    count += 1

            if count == num:
                lucky = max(lucky, num)

        return lucky
```

Time Complexity: $O(n^2)$ Space Complexity: $O(1)$

## 2. Optimal Approach (HashMap)

python

```python
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)

        lucky = -1

        for num, count in freq.items():
            if num == count:
                lucky = max(lucky, num)

        return lucky
```

Time Complexity: $O(n)$ Space Complexity: $O(n)$
