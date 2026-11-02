# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).



# Example 1:

# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
# Example 2:

# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.
# Example 3:

# Input: rating = [1,2,3,4]
# Output: 4


# Constraints:

# n == rating.length
# 3 <= n <= 1000
# 1 <= rating[i] <= 105
# All the integers in rating are unique.
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
# ## 1. Brute Force Approach (3 Loops)

python

```python
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    if (rating[i] < rating[j] < rating[k] or
                        rating[i] > rating[j] > rating[k]):
                        count += 1

        return count
```

Time Complexity: $O(n^3)$ Space Complexity: $O(1)$

## 2. Optimal Approach (Counting Smaller and Greater)

python

```python
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0

        for j in range(n):
            left_smaller = 0
            left_greater = 0
            right_smaller = 0
            right_greater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                else:
                    left_greater += 1

            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_smaller += 1
                else:
                    right_greater += 1

            count += (left_smaller * right_greater)
            count += (left_greater * right_smaller)

        return count
```

Time Complexity: $O(n^2)$ Space Complexity: $O(1)$
