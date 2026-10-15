# We are given hours, a list of the number of hours worked per day for a given employee.

# A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

# A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

# Return the length of the longest well-performing interval.



# Example 1:

# Input: hours = [9,9,6,0,6,6,9]
# Output: 3
# Explanation: The longest well-performing interval is [9,9,6].
# Example 2:

# Input: hours = [6,6,6]
# Output: 0


# Constraints:

# 1 <= hours.length <= 104
# 0 <= hours[i] <= 16
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
# ### Brute Force — O(n²)

python
```
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        ans = 0

        for i in range(n):
            tiring = 0
            non_tiring = 0

            for j in range(i, n):
                if hours[j] > 8:
                    tiring += 1
                else:
                    non_tiring += 1

                if tiring > non_tiring:
                    ans = max(ans, j - i + 1)

        return ans
```

### Optimal — O(n)

python
```
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        prefix = 0
        first = {}
        ans = 0

        for i, h in enumerate(hours):
            prefix += 1 if h > 8 else -1

            if prefix > 0:
                ans = i + 1
            else:
                if prefix - 1 in first:
                    ans = max(ans, i - first[prefix - 1])

            if prefix not in first:
                first[prefix] = i

        return ans
```
