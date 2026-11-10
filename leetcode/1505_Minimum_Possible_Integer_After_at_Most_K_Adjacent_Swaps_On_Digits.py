# You are given a string num representing the digits of a very large integer and an integer k. You are allowed to swap any two adjacent digits of the integer at most k times.

# Return the minimum integer you can obtain also as a string.



# Example 1:


# Input: num = "4321", k = 4
# Output: "1342"
# Explanation: The steps to obtain the minimum integer from 4321 with 4 adjacent swaps are shown.
# Example 2:

# Input: num = "100", k = 1
# Output: "010"
# Explanation: It's ok for the output to have leading zeros, but the input is guaranteed not to have any leading zeros.
# Example 3:

# Input: num = "36789", k = 1000
# Output: "36789"
# Explanation: We can keep the number without any swaps.


# Constraints:

# 1 <= num.length <= 3 * 104
# num consists of only digits and does not contain leading zeros.
# 1 <= k <= 109
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
# ### 1. Brute Force (Greedy)

python

```python
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        arr = list(num)
        n = len(arr)

        for i in range(n):
            if k == 0:
                break

            min_idx = i

            for j in range(i + 1, min(n, i + k + 1)):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            for j in range(min_idx, i, -1):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

            k -= min_idx - i

        return ''.join(arr)
```

### 2. Optimal Solution (Greedy + Fenwick Tree)

from collections import deque

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        pos = [deque() for _ in range(10)]

        for i, ch in enumerate(num):
            pos[int(ch)].append(i)

        bit = FenwickTree(n)

        for i in range(1, n + 1):
            bit.update(i, 1)

        ans = []

        for _ in range(n):
            for d in range(10):
                if not pos[d]:
                    continue

                idx = pos[d][0]
                cost = bit.query(idx + 1) - 1

                if cost <= k:
                    k -= cost
                    ans.append(str(d))
                    pos[d].popleft()
                    bit.update(idx + 1, -1)
                    break

        return ''.join(ans)
