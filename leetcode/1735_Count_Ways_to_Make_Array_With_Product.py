# You are given a 2D integer array, queries. For each queries[i], where queries[i] = [ni, ki], find the number of different ways you can place positive integers into an array of size ni such that the product of the integers is ki. As the number of ways may be too large, the answer to the ith query is the number of ways modulo 109 + 7.

# Return an integer array answer where answer.length == queries.length, and answer[i] is the answer to the ith query.



# Example 1:

# Input: queries = [[2,6],[5,1],[73,660]]
# Output: [4,1,50734910]
# Explanation: Each query is independent.
# [2,6]: There are 4 ways to fill an array of size 2 that multiply to 6: [1,6], [2,3], [3,2], [6,1].
# [5,1]: There is 1 way to fill an array of size 5 that multiply to 1: [1,1,1,1,1].
# [73,660]: There are 1050734917 ways to fill an array of size 73 that multiply to 660. 1050734917 modulo 109 + 7 = 50734910.
# Example 2:

# Input: queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# Output: [1,2,3,10,5]


# Constraints:

# 1 <= queries.length <= 104
# 1 <= ni, ki <= 104
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
# ### 1. Brute Force — Python

python

```python

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        ans = []

        for n, k in queries:
            factors = []

            d = 2
            while d * d <= k:
                count = 0

                while k % d == 0:
                    count += 1
                    k //= d

                if count:
                    factors.append(count)

                d += 1

            if k > 1:
                factors.append(1)

            result = 1

            for p in factors:
                result = result * comb(n + p - 1, p) % MOD

            ans.append(result)

        return ans
```

### 2. Optimal — Python

Recommendedpython

```python

from typing import List
from math import comb

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        MAX = 10004

        spf = list(range(MAX))

        for i in range(2, int(MAX**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, MAX, i):
                    if spf[j] == j:
                        spf[j] = i

        ans = []

        for n, k in queries:
            result = 1

            while k > 1:
                p = spf[k]
                count = 0

                while k % p == 0:
                    k //= p
                    count += 1

                result = result * comb(n + count - 1, count) % MOD

            ans.append(result)

        return ans
```

Complexity:

- Brute Force: O(Q × √K)
- Optimal: O(MAX log log MAX + Q × log K)
- Space: O(MAX + Q) for optimal.
