# Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

# Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array, format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

# Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.



# Example 1:

# Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
# Output: [1,0,0,0,0]
# Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.
# Example 2:

# Input: arr1 = [0], arr2 = [0]
# Output: [0]
# Example 3:

# Input: arr1 = [0], arr2 = [1]
# Output: [1]


# Constraints:

# 1 <= arr1.length, arr2.length <= 1000
# arr1[i] and arr2[i] are 0 or 1
# arr1 and arr2 have no leading zeros
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
# ### Brute Force

python
```
class Solution:
    def addNegabinary(self, arr1: list[int], arr2: list[int]) -> list[int]:
        def convert(arr):
            num = 0
            for bit in arr:
                num = num * (-2) + bit
            return num

        num = convert(arr1) + convert(arr2)

        if num == 0:
            return [0]

        ans = []
        while num != 0:
            remainder = num % 2
            ans.append(remainder)
            num = (num - remainder) // -2

        return ans[::-1]
```

### Optimal (Direct Addition)

python
```
class Solution:
    def addNegabinary(self, arr1: list[int], arr2: list[int]) -> list[int]:
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += arr1[i]
                i -= 1

            if j >= 0:
                total += arr2[j]
                j -= 1

            ans.append(total & 1)
            carry = -(total >> 1)

        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()

        return ans[::-1]
```
