# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.



# Example 1:

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:

# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]


# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 9
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
# ### Brute Force

python
```
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0

        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                arr.pop()
                i += 2
            else:
                i += 1
```

### Optimal

python
```
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        zeros = arr.count(0)
        i = n - 1
        j = n + zeros - 1

        while i < j:
            if j < n:
                arr[j] = arr[i]

            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0

            i -= 1
            j -= 1
```
