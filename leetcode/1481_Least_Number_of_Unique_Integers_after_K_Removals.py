# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.



# Example 1:

# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.


# Constraints:

# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^9
# 0 <= k <= arr.length
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
# ### 1. Brute Force Approach (Frequency + Sorting)

python

```python
from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = list(Counter(arr).values())
        freq.sort()

        unique = len(freq)

        for count in freq:
            if k >= count:
                k -= count
                unique -= 1
            else:
                break

        return unique
```

Time Complexity: O(n log n)

Space Complexity: O(n)

### 2. Optimal Approach (Min Heap)

python

```python
from typing import List
from collections import Counter
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = list(Counter(arr).values())
        heapq.heapify(freq)

        unique = len(freq)

        while freq and k > 0:
            count = heapq.heappop(freq)

            if k >= count:
                k -= count
                unique -= 1
            else:
                break

        return unique
```

Time Complexity: O(n + u log u), where u is the number of unique elements.

Space Complexity: O(u)
