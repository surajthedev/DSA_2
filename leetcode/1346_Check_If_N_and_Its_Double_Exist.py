# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]


# Example 1:

# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
# Example 2:

# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.


# Constraints:

# 2 <= arr.length <= 500
# -103 <= arr[i] <= 103
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
# ### 1. Brute Force – O(n²)

python

```
class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        n = len(arr)

        for i in range(n):
            for j in range(n):
                if i != j and arr[i] == 2 * arr[j]:
                    return True

        return False
```

### 2. Optimal – O(n) Time, O(n) Space

python

```
class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = set()

        for num in arr:
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True

            seen.add(num)

        return False
```
