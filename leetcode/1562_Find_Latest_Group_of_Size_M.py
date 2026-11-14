# Given an array arr that represents a permutation of numbers from 1 to n.

# You have a binary string of size n that initially has all its bits set to zero. At each step i (assuming both the binary string and arr are 1-indexed) from 1 to n, the bit at position arr[i] is set to 1.

# You are also given an integer m. Find the latest step at which there exists a group of ones of length m. A group of ones is a contiguous substring of 1's such that it cannot be extended in either direction.

# Return the latest step at which there exists a group of ones of length exactly m. If no such group exists, return -1.



# Example 1:

# Input: arr = [3,5,1,2,4], m = 1
# Output: 4
# Explanation:
# Step 1: "00100", groups: ["1"]
# Step 2: "00101", groups: ["1", "1"]
# Step 3: "10101", groups: ["1", "1", "1"]
# Step 4: "11101", groups: ["111", "1"]
# Step 5: "11111", groups: ["11111"]
# The latest step at which there exists a group of size 1 is step 4.
# Example 2:

# Input: arr = [3,1,5,4,2], m = 2
# Output: -1
# Explanation:
# Step 1: "00100", groups: ["1"]
# Step 2: "10100", groups: ["1", "1"]
# Step 3: "10101", groups: ["1", "1", "1"]
# Step 4: "10111", groups: ["1", "111"]
# Step 5: "11111", groups: ["11111"]
# No group of size 2 exists during any step.


# Constraints:

# n == arr.length
# 1 <= m <= n <= 105
# 1 <= arr[i] <= n
# All integers in arr are distinct.
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
#
#
#
#
# ### 1. Brute Force Approach

python

```python
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        bits = [0] * n
        ans = -1

        for step, pos in enumerate(arr, 1):
            bits[pos - 1] = 1

            for i in range(n - m + 1):
                if all(bits[i:i + m]):
                    left = i == 0 or bits[i - 1] == 0
                    right = i + m == n or bits[i + m] == 0

                    if left and right:
                        ans = step
                        break

        return ans
```

Time Complexity: O(n² × m) Space Complexity: O(n)

### 2. Optimal Approach (Group Length Tracking)

python

```python
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)

        if m == n:
            return n

        length = [0] * (n + 2)
        count = [0] * (n + 1)

        ans = -1

        for step, pos in enumerate(arr, 1):
            left = length[pos - 1]
            right = length[pos + 1]

            new_len = left + right + 1

            length[pos - left] = new_len
            length[pos + right] = new_len

            count[left] -= 1
            count[right] -= 1
            count[new_len] += 1

            if count[m] > 0:
                ans = step

        return ans
```

Time Complexity: O(n) Space Complexity: O(n)
