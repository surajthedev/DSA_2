# A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

# Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

# Return the maximum sum of like-time coefficient that the chef can obtain after preparing some amount of dishes.

# Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.



# Example 1:

# Input: satisfaction = [-1,-8,0,5,-9]
# Output: 14
# Explanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
# Each dish is prepared in one unit of time.
# Example 2:

# Input: satisfaction = [4,3,2]
# Output: 20
# Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
# Example 3:

# Input: satisfaction = [-1,-4,-5]
# Output: 0
# Explanation: People do not like the dishes. No dish is prepared.


# Constraints:

# n == satisfaction.length
# 1 <= n <= 500
# -1000 <= satisfaction[i] <= 1000
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
# ## 1. Brute Force Approach (Recursion)

python

```python
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)

        def solve(index, time):
            if index == n:
                return 0

            # Skip current dish
            skip = solve(index + 1, time)

            # Cook current dish
            take = satisfaction[index] * time + solve(index + 1, time + 1)

            return max(skip, take)

        return solve(0, 1)
```

Time Complexity: $O(2^n)$ Space Complexity: $O(n)$

## 2. Optimal Approach (Greedy)

python

```python
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        total = 0
        result = 0

        for value in satisfaction:
            total += value

            if total > 0:
                result += total
            else:
                break

        return result
```

Time Complexity: $O(n \log n)$ Space Complexity: $O(1)$ auxiliary space (sorting excluded).
