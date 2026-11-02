# You are given an integer n.

# We need to group the numbers from 1 to n according to the sum of its digits. For example, the numbers 14 and 5 belong to the same group, whereas 13 and 3 belong to different groups.

# Return the number of groups that have the largest size, i.e. the maximum number of elements.



# Example 1:

# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with largest size.
# Example 2:

# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.


# Constraints:

# 1 <= n <= 104
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
# ## 1. Brute Force Approach

python

```python
class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}

        for num in range(1, n + 1):
            digit_sum = sum(int(digit) for digit in str(num))

            if digit_sum not in groups:
                groups[digit_sum] = 0

            groups[digit_sum] += 1

        max_size = max(groups.values())

        count = 0
        for size in groups.values():
            if size == max_size:
                count += 1

        return count
```

Time Complexity: $O(n \log n)$ Space Complexity: $O(n)$

## 2. Optimal Approach (HashMap + Digit Sum)

python

```python
class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = [0] * 37

        for num in range(1, n + 1):
            x = num
            digit_sum = 0

            while x > 0:
                digit_sum += x % 10
                x //= 10

            groups[digit_sum] += 1

        max_size = max(groups)

        return groups.count(max_size)
```

Time Complexity: $O(n \log n)$ Space Complexity: $O(1)$
