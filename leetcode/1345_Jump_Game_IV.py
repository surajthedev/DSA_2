# Given an array of integers arr, you are initially positioned at the first index of the array.

# In one step you can jump from index i to index:

# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.

# Notice that you can not jump outside of the array at any time.



# Example 1:

# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
# Example 2:

# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You do not need to jump.
# Example 3:

# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index of the array.


# Constraints:

# 1 <= arr.length <= 5 * 104
# -108 <= arr[i] <= 108
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
# ### Brute Force — BFS

python

```
from collections import deque

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)

        if n == 1:
            return 0

        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j and arr[i] == arr[j]:
                    graph[i].append(j)

            if i > 0:
                graph[i].append(i - 1)
            if i < n - 1:
                graph[i].append(i + 1)

        queue = deque([(0, 0)])
        visited = {0}

        while queue:
            i, steps = queue.popleft()

            if i == n - 1:
                return steps

            for j in graph[i]:
                if j not in visited:
                    visited.add(j)
                    queue.append((j, steps + 1))

        return -1
```

### Optimal — BFS + Hash Map

python

```
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)

        if n == 1:
            return 0

        indices = defaultdict(list)

        for i, value in enumerate(arr):
            indices[value].append(i)

        queue = deque([0])
        visited = {0}
        steps = 0

        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()

                if i == n - 1:
                    return steps

                neighbors = [i - 1, i + 1]

                neighbors.extend(indices[arr[i]])
                indices[arr[i]].clear()

                for j in neighbors:
                    if 0 <= j < n and j not in visited:
                        visited.add(j)
                        queue.append(j)

            steps += 1

        return -1
```
