# You would like to make dessert and are preparing to buy the ingredients. You have n ice cream base flavors and m types of toppings to choose from. You must follow these rules when making your dessert:

# There must be exactly one ice cream base.
# You can add one or more types of topping or have no toppings at all.
# There are at most two of each type of topping.
# You are given three inputs:

# baseCosts, an integer array of length n, where each baseCosts[i] represents the price of the ith ice cream base flavor.
# toppingCosts, an integer array of length m, where each toppingCosts[i] is the price of one of the ith topping.
# target, an integer representing your target price for dessert.
# You want to make a dessert with a total cost as close to target as possible.

# Return the closest possible cost of the dessert to target. If there are multiple, return the lower one.



# Example 1:

# Input: baseCosts = [1,7], toppingCosts = [3,4], target = 10
# Output: 10
# Explanation: Consider the following combination (all 0-indexed):
# - Choose base 1: cost 7
# - Take 1 of topping 0: cost 1 x 3 = 3
# - Take 0 of topping 1: cost 0 x 4 = 0
# Total: 7 + 3 + 0 = 10.
# Example 2:

# Input: baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
# Output: 17
# Explanation: Consider the following combination (all 0-indexed):
# - Choose base 1: cost 3
# - Take 1 of topping 0: cost 1 x 4 = 4
# - Take 2 of topping 1: cost 2 x 5 = 10
# - Take 0 of topping 2: cost 0 x 100 = 0
# Total: 3 + 4 + 10 + 0 = 17. You cannot make a dessert with a total cost of 18.
# Example 3:

# Input: baseCosts = [3,10], toppingCosts = [2,5], target = 9
# Output: 8
# Explanation: It is possible to make desserts with cost 8 and 10. Return 8 as it is the lower cost.


# Constraints:

# n == baseCosts.length
# m == toppingCosts.length
# 1 <= n, m <= 10
# 1 <= baseCosts[i], toppingCosts[i] <= 104
# 1 <= target <= 104
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
#
# ### 1. Brute Force Approach (Recursion)

Time Complexity: $O(n \times 3^m)$

python

```python
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ans = float('inf')

        def dfs(i, cost):
            nonlocal ans

            if abs(cost - target) < abs(ans - target):
                ans = cost
            elif abs(cost - target) == abs(ans - target):
                ans = min(ans, cost)

            if i == len(toppingCosts):
                return

            dfs(i + 1, cost)
            dfs(i + 1, cost + toppingCosts[i])
            dfs(i + 1, cost + 2 * toppingCosts[i])

        for base in baseCosts:
            dfs(0, base)

        return ans
```

### 2. Optimal Approach (Meet in the Middle)

O(n × 3^(m/2) × log(3^(m/2)))python

```python
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        from bisect import bisect_left

        mid = len(toppingCosts) // 2

        def generate(arr):
            sums = [0]

            for cost in arr:
                sums += [x + cost for x in sums]
                sums += [x + 2 * cost for x in sums]

            return sums

        left = generate(toppingCosts[:mid])
        right = sorted(generate(toppingCosts[mid:]))

        ans = min(baseCosts)

        for base in baseCosts:
            for x in left:
                remaining = target - base - x

                idx = bisect_left(right, remaining)

                for j in (idx - 1, idx):
                    if 0 <= j < len(right):
                        total = base + x + right[j]

                        if abs(total - target) < abs(ans - target):
                            ans = total
                        elif abs(total - target) == abs(ans - target):
                            ans = min(ans, total)

        return ans
```
