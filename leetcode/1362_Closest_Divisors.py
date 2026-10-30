# Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

# Return the two integers in any order.



# Example 1:

# Input: num = 8
# Output: [3,3]
# Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
# Example 2:

# Input: num = 123
# Output: [5,25]
# Example 3:

# Input: num = 999
# Output: [40,25]


# Constraints:

# 1 <= num <= 10^9
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
# ### Brute Force Solution

python

```
class Solution:
    def closestDivisors(self, num: int) -> list[int]:
        def findClosest(target):
            for i in range(int(target ** 0.5), 0, -1):
                if target % i == 0:
                    return [i, target // i]

        a = findClosest(num + 1)
        b = findClosest(num + 2)

        if abs(a[0] - a[1]) <= abs(b[0] - b[1]):
            return a

        return b
```

Time Complexity: $O(\sqrt{num})$

### Optimal Solution

python

```
class Solution:
    def closestDivisors(self, num: int) -> list[int]:
        import math

        def findClosest(target):
            for i in range(math.isqrt(target), 0, -1):
                if target % i == 0:
                    return [i, target // i]

        a = findClosest(num + 1)
        b = findClosest(num + 2)

        return min([a, b], key=lambda x: abs(x[0] - x[1]))
```

Time Complexity: $O(\sqrt{num})$

Space Complexity: $O(1)$
