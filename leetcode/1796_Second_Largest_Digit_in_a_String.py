# Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

# An alphanumeric string is a string consisting of lowercase English letters and digits.



# Example 1:

# Input: s = "dfa12321afd"
# Output: 2
# Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
# Example 2:

# Input: s = "abc1111"
# Output: -1
# Explanation: The digits that appear in s are [1]. There is no second largest digit.


# Constraints:

# 1 <= s.length <= 500
# s consists of only lowercase English letters and digits.
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
# ### 1. Brute Force — O(n²)

python

```python
class Solution:
    def secondHighest(self, s: str) -> int:
        digits = []

        for ch in s:
            if ch.isdigit() and int(ch) not in digits:
                digits.append(int(ch))

        digits.sort(reverse=True)

        if len(digits) < 2:
            return -1

        return digits[1]
```

### 2. Optimal — O(n)

python

```python
class Solution:
    def secondHighest(self, s: str) -> int:
        largest = -1
        second = -1

        for ch in s:
            if ch.isdigit():
                num = int(ch)

                if num > largest:
                    second = largest
                    largest = num

                elif largest > num > second:
                    second = num

        return second
```
