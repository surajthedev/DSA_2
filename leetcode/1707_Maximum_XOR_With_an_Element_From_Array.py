# You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].

# The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.

# Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.



# Example 1:

# Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
# Output: [3,3,7]
# Explanation:
# 1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
# 2) 1 XOR 2 = 3.
# 3) 5 XOR 2 = 7.
# Example 2:

# Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
# Output: [15,-1,5]


# Constraints:

# 1 <= nums.length, queries.length <= 105
# queries[i].length == 2
# 0 <= nums[j], xi, mi <= 109
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
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []

        for x, m in queries:
            best = -1

            for num in nums:
                if num <= m:
                    best = max(best, x ^ num)

            ans.append(best)

        return ans
```

Time Complexity: O(n × q)

Space Complexity: O(q)

### 2. Optimal Approach (Sorting + Binary Trie)

Optimalpython

```python

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, num):
        node = self.root

        for i in range(31, -1, -1):
            bit = (num >> i) & 1

            if bit not in node:
                node[bit] = {}

            node = node[bit]

    def getMaxXor(self, num):
        node = self.root
        ans = 0

        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            opposite = 1 - bit

            if opposite in node:
                ans |= (1 << i)
                node = node[opposite]
            else:
                node = node[bit]

        return ans


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()

        sorted_queries = sorted(
            [(m, x, i) for i, (x, m) in enumerate(queries)]
        )

        trie = Trie()
        ans = [-1] * len(queries)

        j = 0

        for m, x, idx in sorted_queries:

            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1

            if j > 0:
                ans[idx] = trie.getMaxXor(x)

        return ans
```

Time Complexity: O(n log n + q log q + (n + q) × 32)

Space Complexity: O(n × 32 + q)
