# Design a data structure that efficiently finds the majority element of a given subarray.

# The majority element of a subarray is an element that occurs threshold times or more in the subarray.

# Implementing the MajorityChecker class:

# MajorityChecker(int[] arr) Initializes the instance of the class with the given array arr.
# int query(int left, int right, int threshold) returns the element in the subarray arr[left...right] that occurs at least threshold times, or -1 if no such element exists.


# Example 1:

# Input
# ["MajorityChecker", "query", "query", "query"]
# [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
# Output
# [null, 1, -1, 2]

# Explanation
# MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1, 1]);
# majorityChecker.query(0, 5, 4); // return 1
# majorityChecker.query(0, 3, 3); // return -1
# majorityChecker.query(2, 3, 2); // return 2


# Constraints:

# 1 <= arr.length <= 2 * 104
# 1 <= arr[i] <= 2 * 104
# 0 <= left <= right < arr.length
# threshold <= right - left + 1
# 2 * threshold > right - left + 1
# At most 104 calls will be made to query.
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
# ### Brute Force — Python

python
```
from collections import Counter

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        freq = Counter(self.arr[left:right + 1])

        for num, count in freq.items():
            if count >= threshold:
                return num

        return -1
```

### Optimal — Python (Boyer-Moore + Binary Search)

python
```
from collections import defaultdict
from bisect import bisect_left, bisect_right
import random

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.positions = defaultdict(list)

        for i, num in enumerate(arr):
            self.positions[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        length = right - left + 1

        for _ in range(40):
            candidate = self.arr[random.randint(left, right)]
            indices = self.positions[candidate]

            count = (
                bisect_right(indices, right)
                - bisect_left(indices, left)
            )

            if count >= threshold:
                return candidate

        return -1
```
