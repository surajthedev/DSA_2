# You are given an integer num. You will apply the following steps to num two separate times:

# Pick a digit x (0 <= x <= 9).
# Pick another digit y (0 <= y <= 9). Note y can be equal to x.
# Replace all the occurrences of x in the decimal representation of num by y.
# Let a and b be the two results from applying the operation to num independently.

# Return the max difference between a and b.

# Note that neither a nor b may have any leading zeros, and must not be 0.



# Example 1:

# Input: num = 555
# Output: 888
# Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
# The second time pick x = 5 and y = 1 and store the new integer in b.
# We have now a = 999 and b = 111 and max difference = 888
# Example 2:

# Input: num = 9
# Output: 8
# Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
# The second time pick x = 9 and y = 1 and store the new integer in b.
# We have now a = 9 and b = 1 and max difference = 8


# Constraints:

# 1 <= num <= 108
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
    def maxDiff(self, num: int) -> int:
        s = str(num)
        max_num = num
        min_num = num

        for x in '0123456789':
            for y in '0123456789':
                if s[0] == x and y == '0':
                    continue

                temp = s.replace(x, y)

                if temp[0] == '0':
                    continue

                value = int(temp)

                max_num = max(max_num, value)
                min_num = min(min_num, value)

        return max_num - min_num
```

Time Complexity: $O(100 \times n)$

Space Complexity: $O(n)$

### 2. Optimal Approach (Greedy)

python

```python
class Solution:
    def maxDiff(self, num: int) -> int:
        s = list(str(num))

        # Find maximum number
        max_s = s[:]

        for ch in max_s:
            if ch != '9':
                x = ch
                break
        else:
            x = None

        if x is not None:
            max_s = ['9' if ch == x else ch for ch in max_s]

        # Find minimum number
        min_s = s[:]

        if min_s[0] != '1':
            x = min_s[0]
            min_s = ['1' if ch == x else ch for ch in min_s]
        else:
            for ch in min_s[1:]:
                if ch not in ('0', '1'):
                    x = ch
                    min_s = ['0' if c == x else c for c in min_s]
                    break

        return int(''.join(max_s)) - int(''.join(min_s))
```

Time Complexity: $O(n)$

Space Complexity: $O(n)$
