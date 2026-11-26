# There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

# You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

# It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

# Return the original array nums. If there are multiple solutions, return any of them.



# Example 1:

# Input: adjacentPairs = [[2,1],[3,4],[3,2]]
# Output: [1,2,3,4]
# Explanation: This array has all its adjacent pairs in adjacentPairs.
# Notice that adjacentPairs[i] may not be in left-to-right order.
# Example 2:

# Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
# Output: [-2,4,1,-3]
# Explanation: There can be negative numbers.
# Another solution is [-3,1,4,-2], which would also be accepted.
# Example 3:

# Input: adjacentPairs = [[100000,-100000]]
# Output: [100000,-100000]


# Constraints:

# nums.length == n
# adjacentPairs.length == n - 1
# adjacentPairs[i].length == 2
# 2 <= n <= 105
# -105 <= nums[i], ui, vi <= 105
# There exists some nums that has adjacentPairs as its pairs.
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
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        nums = []
        for a, b in adjacentPairs:
            if a not in nums:
                nums.append(a)
            if b not in nums:
                nums.append(b)

        result = [nums[0]]
        visited = {nums[0]}

        while len(result) < len(nums):
            for a, b in adjacentPairs:
                if a == result[-1] and b not in visited:
                    result.append(b)
                    visited.add(b)
                    break
                elif b == result[-1] and a not in visited:
                    result.append(a)
                    visited.add(a)
                    break

        return result
```

### Optimal (HashMap + Graph)

python

```python
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = {}

        for a, b in adjacentPairs:
            graph.setdefault(a, []).append(b)
            graph.setdefault(b, []).append(a)

        start = next(num for num in graph if len(graph[num]) == 1)

        result = [start]
        prev = None
        curr = start

        while len(result) < len(graph):
            for neighbor in graph[curr]:
                if neighbor != prev:
                    result.append(neighbor)
                    prev, curr = curr, neighbor
                    break

        return result
```
