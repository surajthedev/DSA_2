# Given a (0-indexed) integer array nums and two integers low and high, return the number of nice pairs.

# A nice pair is a pair (i, j) where 0 <= i < j < nums.length and low <= (nums[i] XOR nums[j]) <= high.



# Example 1:

# Input: nums = [1,4,2,7], low = 2, high = 6
# Output: 6
# Explanation: All nice pairs (i, j) are as follows:
#     - (0, 1): nums[0] XOR nums[1] = 5
#     - (0, 2): nums[0] XOR nums[2] = 3
#     - (0, 3): nums[0] XOR nums[3] = 6
#     - (1, 2): nums[1] XOR nums[2] = 6
#     - (1, 3): nums[1] XOR nums[3] = 3
#     - (2, 3): nums[2] XOR nums[3] = 5
# Example 2:

# Input: nums = [9,8,4,2,1], low = 5, high = 14
# Output: 8
# Explanation: All nice pairs (i, j) are as follows:
# ​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
#     - (0, 3): nums[0] XOR nums[3] = 11
#     - (0, 4): nums[0] XOR nums[4] = 8
#     - (1, 2): nums[1] XOR nums[2] = 12
#     - (1, 3): nums[1] XOR nums[3] = 10
#     - (1, 4): nums[1] XOR nums[4] = 9
#     - (2, 3): nums[2] XOR nums[3] = 6
#     - (2, 4): nums[2] XOR nums[4] = 5


# Constraints:

# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 2 * 104
# 1 <= low <= high <= 2 * 104
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
# ### Brute Force

python

```python

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                xor = nums[i] ^ nums[j]

                if low <= xor <= high:
                    ans += 1

        return ans
```

Time Complexity: O(n²) Space Complexity: O(1)

### Optimal (Binary Trie)

Optimalpython

```python

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:

        class Trie:
            def __init__(self):
                self.root = {}

            def insert(self, num):
                node = self.root

                for i in range(15, -1, -1):
                    bit = (num >> i) & 1

                    if bit not in node:
                        node[bit] = {}

                    node = node[bit]

                node["count"] = node.get("count", 0) + 1

            def countLess(self, num, limit):
                node = self.root
                count = 0

                for i in range(15, -1, -1):
                    if not node:
                        break

                    bit = (num >> i) & 1
                    limit_bit = (limit >> i) & 1

                    if limit_bit == 1:
                        if bit in node:
                            count += node[bit].get("count", 0)

                        node = node.get(1 - bit)
                    else:
                        node = node.get(bit)

                return count

        trie = Trie()
        ans = 0

        for num in nums:
            ans += trie.countLess(num, high + 1)
            ans -= trie.countLess(num, low)
            trie.insert(num)

        return ans
```

Time Complexity: O(n × 16) = O(n log M) Space Complexity: O(n × 16)
