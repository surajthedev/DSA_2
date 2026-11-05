# Given an array of integers arr.

# We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

# Let's define a and b as follows:

# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# Note that ^ denotes the bitwise-xor operation.

# Return the number of triplets (i, j and k) Where a == b.



# Example 1:

# Input: arr = [2,3,1,6,7]
# Output: 4
# Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
# Example 2:

# Input: arr = [1,1,1,1,1]
# Output: 10


# Constraints:

# 1 <= arr.length <= 300
# 1 <= arr[i] <= 108
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
# ### 1. Brute Force Approach — Prefix XOR

python

```python
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                a = 0

                for x in range(i, j):
                    a ^= arr[x]

                b = 0

                for k in range(j, n):
                    b ^= arr[k]

                    if a == b:
                        ans += 1

        return ans
```

Time Complexity: O(n³)

Space Complexity: O(1)

### 2. Optimal Approach — Prefix XOR + Counting

python

```python
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]

        ans = 0

        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    ans += k - i

        return ans
```

Time Complexity: O(n²)

Space Complexity: O(n)

### 3. More Optimal Approach — One Pass

python

```python
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = {0: 1}
        total = {0: 0}

        xor = 0
        ans = 0

        for i, num in enumerate(arr):
            xor ^= num

            if xor in count:
                ans += count[xor] * i - total[xor]

            count[xor] = count.get(xor, 0) + 1
            total[xor] = total.get(xor, 0) + i + 1

        return ans
```

Time Complexity: O(n)

Space Complexity: O(n)
