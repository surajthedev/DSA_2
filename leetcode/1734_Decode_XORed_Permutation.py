# There is an integer array perm that is a permutation of the first n positive integers, where n is always odd.

# It was encoded into another integer array encoded of length n - 1, such that encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then encoded = [2,1].

# Given the encoded array, return the original array perm. It is guaranteed that the answer exists and is unique.



# Example 1:

# Input: encoded = [3,1]
# Output: [1,2,3]
# Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
# Example 2:

# Input: encoded = [6,5,4,6]
# Output: [2,4,1,5,3]


# Constraints:

# 3 <= n < 105
# n is odd.
# encoded.length == n - 1
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
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1

        for first in range(1, n + 1):
            perm = [first]

            for x in encoded:
                perm.append(perm[-1] ^ x)

            if sorted(perm) == list(range(1, n + 1)):
                return perm
```

- Time Complexity: O(N² log N)
- Space Complexity: O(N)

### 2. Optimal — Python

Recommendedpython

```python

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1

        total = 0
        for i in range(1, n + 1):
            total ^= i

        xor = 0
        for i in range(1, len(encoded), 2):
            xor ^= encoded[i]

        first = total ^ xor

        perm = [first]

        for x in encoded:
            perm.append(perm[-1] ^ x)

        return perm
```

- Time Complexity: O(N)
- Space Complexity: O(N) (output array).
