# You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

# Return true if it is possible to form the array arr from pieces. Otherwise, return false.



# Example 1:

# Input: arr = [15,88], pieces = [[88],[15]]
# Output: true
# Explanation: Concatenate [15] then [88]
# Example 2:

# Input: arr = [49,18,16], pieces = [[16,18,49]]
# Output: false
# Explanation: Even though the numbers match, we cannot reorder pieces[0].
# Example 3:

# Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
# Output: true
# Explanation: Concatenate [91] then [4,64] then [78]


# Constraints:

# 1 <= pieces.length <= arr.length <= 100
# sum(pieces[i].length) == arr.length
# 1 <= pieces[i].length <= arr.length
# 1 <= arr[i], pieces[i][j] <= 100
# The integers in arr are distinct.
# The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).
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
#
# ### 1. Brute Force Solution

python

```python
from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        used = [False] * len(pieces)
        result = []

        while len(result) < len(arr):
            found = False

            for i in range(len(pieces)):
                if not used[i] and pieces[i][0] == arr[len(result)]:
                    result.extend(pieces[i])
                    used[i] = True
                    found = True
                    break

            if not found:
                return False

        return result == arr
```

Time Complexity: O(n²)

Space Complexity: O(n)

### 2. Optimal Solution (HashMap)

python

```python
from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {piece[0]: piece for piece in pieces}

        i = 0

        while i < len(arr):
            if arr[i] not in mp:
                return False

            piece = mp[arr[i]]

            for num in piece:
                if i >= len(arr) or arr[i] != num:
                    return False
                i += 1

        return True
```

Time Complexity: O(n)

Space Complexity: O(n)
