# There is a pizza with 3n slices of varying size, you and your friends will take slices of pizza as follows:

# You will pick any pizza slice.
# Your friend Alice will pick the next slice in the anti-clockwise direction of your pick.
# Your friend Bob will pick the next slice in the clockwise direction of your pick.
# Repeat until there are no more slices of pizzas.
# Given an integer array slices that represent the sizes of the pizza slices in a clockwise direction, return the maximum possible sum of slice sizes that you can pick.



# Example 1:


# Input: slices = [1,2,3,4,5,6]
# Output: 10
# Explanation: Pick pizza slice of size 4, Alice and Bob will pick slices with size 3 and 5 respectively. Then Pick slices with size 6, finally Alice and Bob will pick slice of size 2 and 1 respectively. Total = 4 + 6.
# Example 2:


# Input: slices = [8,9,8,6,1,1]
# Output: 16
# Explanation: Pick pizza slice of size 8 in each turn. If you pick slice with size 9 your partners will pick slices of size 8.


# Constraints:

# 3 * n == slices.length
# 1 <= slices.length <= 500
# 1 <= slices[i] <= 1000
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
# ### Brute Force Approach (Recursion)

python

```python
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices) // 3

        def solve(start, end, k):
            if k == 0 or start > end:
                return 0

            take = slices[start] + solve(start + 2, end, k - 1)
            not_take = solve(start + 1, end, k)

            return max(take, not_take)

        return max(
            solve(0, len(slices) - 2, n),
            solve(1, len(slices) - 1, n)
        )
```

### Optimal Approach (Dynamic Programming + Space Optimization)

python

```python
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices) // 3

        def solve(arr):
            m = len(arr)

            dp = [[0] * (n + 1) for _ in range(m + 2)]

            for i in range(m - 1, -1, -1):
                for k in range(1, n + 1):
                    take = arr[i] + dp[i + 2][k - 1]
                    not_take = dp[i + 1][k]

                    dp[i][k] = max(take, not_take)

            return dp[0][n]

        return max(
            solve(slices[:-1]),
            solve(slices[1:])
        )
```
