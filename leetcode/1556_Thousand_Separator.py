# Given an integer n, add a dot (".") as the thousands separator and return it in string format.



# Example 1:

# Input: n = 987
# Output: "987"
# Example 2:

# Input: n = 1234
# Output: "1.234"


# Constraints:

# 0 <= n <= 231 - 1
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
# ### Brute Force — O(log n)

python

```python
class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        result = ""

        count = 0

        for i in range(len(s) - 1, -1, -1):
            result = s[i] + result
            count += 1

            if count == 3 and i != 0:
                result = "." + result
                count = 0

        return result
```

### Optimal — O(log n)

python

```python
class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f"{n:,}".replace(",", ".")
```
