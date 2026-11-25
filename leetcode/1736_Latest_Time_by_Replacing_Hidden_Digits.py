# You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).

# The valid times are those inclusively between 00:00 and 23:59.

# Return the latest valid time you can get from time by replacing the hidden digits.



# Example 1:

# Input: time = "2?:?0"
# Output: "23:50"
# Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
# Example 2:

# Input: time = "0?:3?"
# Output: "09:39"
# Example 3:

# Input: time = "1?:22"
# Output: "19:22"


# Constraints:

# time is in the format hh:mm.
# It is guaranteed that you can produce a valid time from the given string.
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
# ### 1. Brute Force — Python

python

```python

class Solution:
    def maximumTime(self, time: str) -> str:
        ans = ""

        for h in range(23, -1, -1):
            for m in range(59, -1, -1):
                candidate = f"{h:02d}:{m:02d}"

                valid = True

                for i in range(5):
                    if time[i] != '?' and time[i] != candidate[i]:
                        valid = False
                        break

                if valid:
                    return candidate

        return ans
```

- Time Complexity: O(24 × 60)
- Space Complexity: O(1)

### 2. Optimal — Python

Recommendedpython

```python

class Solution:
    def maximumTime(self, time: str) -> str:
        t = list(time)

        if t[0] == '?':
            t[0] = '2' if t[1] == '?' or t[1] <= '3' else '1'

        if t[1] == '?':
            t[1] = '3' if t[0] == '2' else '9'

        if t[3] == '?':
            t[3] = '5'

        if t[4] == '?':
            t[4] = '9'

        return ''.join(t)
```

- Time Complexity: O(1)
- Space Complexity: O(1)
