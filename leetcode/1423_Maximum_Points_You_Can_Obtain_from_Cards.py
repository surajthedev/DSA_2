# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.

# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.



# Example 1:

# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
# Example 2:

# Input: cardPoints = [2,2,2], k = 2
# Output: 4
# Explanation: Regardless of which two cards you take, your score will always be 4.
# Example 3:

# Input: cardPoints = [9,7,7,9,7,7,9], k = 7
# Output: 55
# Explanation: You have to take all the cards. Your score is the sum of points of all cards.


# Constraints:

# 1 <= cardPoints.length <= 105
# 1 <= cardPoints[i] <= 104
# 1 <= k <= cardPoints.length
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
# ### 1. Brute Force Approach

python

```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        max_score = 0

        for i in range(k + 1):
            left_sum = sum(cardPoints[:i])
            right_sum = sum(cardPoints[n - (k - i):]) if k - i > 0 else 0

            max_score = max(max_score, left_sum + right_sum)

        return max_score
```

Time Complexity: $O(k^2)$

Space Complexity: $O(k)$

### 2. Optimal Approach (Sliding Window)

python

```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window_size = n - k

        total_sum = sum(cardPoints)
        window_sum = sum(cardPoints[:window_size])

        min_sum = window_sum

        for i in range(window_size, n):
            window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_sum = min(min_sum, window_sum)

        return total_sum - min_sum
```

Time Complexity: $O(n)$

Space Complexity: $O(1)$
