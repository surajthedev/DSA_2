# Given an array of integers arr of even length n and an integer k.

# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

# Return true If you can find a way to do that or false otherwise.



# Example 1:

# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
# Example 2:

# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).
# Example 3:

# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.


# Constraints:

# arr.length == n
# 1 <= n <= 105
# n is even.
# -109 <= arr[i] <= 109
# 1 <= k <= 105
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
# ### 1. Brute Force — O(n²)

python

```python

from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        used = [False] * len(arr)

        for i in range(len(arr)):
            if used[i]:
                continue

            found = False

            for j in range(i + 1, len(arr)):
                if not used[j] and (arr[i] + arr[j]) % k == 0:
                    used[i] = True
                    used[j] = True
                    found = True
                    break

            if not found:
                return False

        return True
```

### 2. Optimal — O(n + k)

python

```python

from typing import List
from collections import Counter

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = Counter(x % k for x in arr)

        if freq[0] % 2 != 0:
            return False

        if k % 2 == 0 and freq[k // 2] % 2 != 0:
            return False

        for r in range(1, (k + 1) // 2):
            if freq[r] != freq[k - r]:
                return False

        return True
```
